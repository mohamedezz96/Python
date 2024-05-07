import subprocess
import json
import boto3
import base64
import os
import re
from botocore.signers import RequestSigner
from kubernetes import client
from kubernetes.client.rest import ApiException

# the cluster name
cluster_name = os.environ["CLUSTER_NAME"]
# the AWS region
aws_region = os.environ["AWS_REGION"]
# the filesystem id
efs_filesystem_id = 'fs-0eba6c8d5dc11b833'

def get_bearer_token():
    STS_TOKEN_EXPIRES_IN = 60
    session = boto3.session.Session(region_name=aws_region)

    client = session.client('sts')
    service_id = client.meta.service_model.service_id

    signer = RequestSigner(
        service_id,
        aws_region,
        'sts',
        'v4',
        session.get_credentials(),
        session.events
    )

    params = {
        'method': 'GET',
        'url': 'https://sts.{}.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15'.format(aws_region),
        'body': {},
        'headers': {
            'x-k8s-aws-id': cluster_name
        },
        'context': {}
    }

    signed_url = signer.generate_presigned_url(
        params,
        region_name=aws_region,
        expires_in=STS_TOKEN_EXPIRES_IN,
        operation_name=''
    )

    base64_url = base64.urlsafe_b64encode(signed_url.encode('utf-8')).decode('utf-8')

    # remove any base64 encoding padding:
    return 'k8s-aws-v1.' + re.sub(r'=*', '', base64_url)


def get_pv_info_cluster():
    eks = boto3.client('eks', region_name=aws_region)
    cluster_info = eks.describe_cluster(name=cluster_name)
    cluster_endpoint = cluster_info['cluster']['endpoint']
    cert_authority = cluster_info['cluster']['certificateAuthority']['data']
    with open('/tmp/ca.crt', 'wb') as f:
        f.write(base64.b64decode(cert_authority))

    configuration = client.Configuration()
    configuration.api_key['authorization'] = get_bearer_token()
    configuration.api_key_prefix['authorization'] = 'Bearer'
    configuration.host = cluster_endpoint
    configuration.ssl_ca_cert = '/tmp/ca.crt'

    # Initialize an empty list to store volume handles
    volume_handles = []

    # Enter a context with an instance of the API kubernetes.client
    with client.ApiClient(configuration) as api_client:
        api_instance = client.CoreV1Api(api_client)
        try:
            api_response = api_instance.list_persistent_volume()
            print("Listing persistent volumes:")
            for pv in api_response.items:
                print("Name: %s, Capacity: %s, Status: %s, VolumeHandles: %s" % (pv.metadata.name, pv.spec.capacity, pv.status.phase, pv.spec.csi.volume_handle))
                # Append volume handle to the list
                volume_handles.append(pv.spec.csi.volume_handle)

            # Print the list of volume handles
            print("Volume Handles:", volume_handles)

        except ApiException as e:
            print("Exception when calling CoreV1Api->list_persistent_volume: %s\n" % e)
        return volume_handles

def extract_pv_access_point_id_cluster(volume_handles):
    # Initialize an empty list to store volumeHandles
    pv_access_point_id_cluster = []

    # Iterate over items in the JSON
    for item in volume_handles:
        fsap_index = item.find('fsap-')
        if fsap_index != -1:
            pv_access_point_id_cluster.append(item[fsap_index:])
    
    return pv_access_point_id_cluster

def get_pv_info_aws(efs_filesystem_id):
    # Initialize boto3 EFS client
    efs_client = boto3.client('efs')

    # Describe access points of the EFS filesystem
    access_point_output = efs_client.describe_access_points(FileSystemId=efs_filesystem_id, MaxResults=1000)

    return access_point_output

def extract_pv_access_point_id_aws(access_point_output):
    # Extract access point IDs from the response
    access_point_ids = [access_point["AccessPointId"] for access_point in access_point_output["AccessPoints"]]

    return access_point_ids

def find_unique_ids(pv_access_point_id_cluster, pv_access_point_id_aws):
    # Find paths that are in modified_paths but not in pv_names
    deprecated_access_points_ids = [pv_access_point_id_aws for pv_access_point_id_aws in pv_access_point_id_aws if pv_access_point_id_aws not in pv_access_point_id_cluster]
    return deprecated_access_points_ids

def delete_access_points(deprecated_access_point_ids):
    # Initialize boto3 EFS client
    efs_client = boto3.client('efs')

    # Iterate over each access point ID and delete it
    for access_point_id in deprecated_access_point_ids:
        efs_client.delete_access_point(AccessPointId=access_point_id)

def lambda_handler(event, context):
    # Get the PV info from the cluster
    volume_handles=get_pv_info_cluster()
    print(volume_handles)

    # Extract the PV access point id
    pv_access_point_id_cluster=extract_pv_access_point_id_cluster(volume_handles)
    print(pv_access_point_id_cluster)

    # Run the AWS command
    pv_info_aws= get_pv_info_aws(efs_filesystem_id)
    print(pv_info_aws)

    # Extract the access point path
    pv_access_point_id_aws = extract_pv_access_point_id_aws(pv_info_aws)
    print(pv_access_point_id_aws)

    # Find deprecated access points
    deprecated_access_point_ids = find_unique_ids(pv_access_point_id_cluster, pv_access_point_id_aws)
    print(deprecated_access_point_ids)

    # Delete deprecated access points
    delete_access_points(deprecated_access_point_ids)

    return {
        'statusCode': 200,
        'body': json.dumps('Deprecated access points deleted successfully!')
    }
