import subprocess
import json

def get_pv_info():
    # Run the kubectl get pv -o json command and capture the output
    pv_output = subprocess.run(['kubectl', 'get', 'pv', '-o', 'json'], capture_output=True, text=True).stdout
    
    # Parse the JSON output
    pv_info = json.loads(pv_output)
    
    return pv_info

def extract_pv_access_point_id(pv_info):
    # Initialize an empty list to store volumeHandles
    volume_handles = []

    # Iterate over items in the JSON
    for item in pv_info["items"]:
        # Extract the volumeHandle
        volume_handle = item["spec"]["csi"]["volumeHandle"]
        # Append the volumeHandle to the list
        volume_handles.append(volume_handle)

    # Iterate over the volume_handles list
    for i in range(len(volume_handles)):
        # Split the value using '::' as delimiter and extract the substring starting with 'fsap-'
        _, value = volume_handles[i].split('::')
        volume_handles[i] = value

    return volume_handles

def run_aws_command(efs_filesystem_id, profile):
    # Run the AWS CLI command to describe the access points of the EFS filesystem
    aws_command = ['aws', 'efs', 'describe-access-points', '--file-system-id', efs_filesystem_id, '--profile', profile, '--max-result', '1000']
    access_point_output = subprocess.run(aws_command, capture_output=True, text=True).stdout
    
    return access_point_output

def extract_access_point_ids(access_point_output):
    # Parse the JSON output to get the access point path
    access_point_info = json.loads(access_point_output)
    access_point_ids = [access_point["AccessPointId"] for access_point in access_point_info["AccessPoints"]]
    
    return access_point_ids

def find_unique_ids(pv_access_point_ids, access_point_ids):
    # Find paths that are in modified_paths but not in pv_names
    deprecated_access_points_ids = [access_point_id for access_point_id in access_point_ids if access_point_id not in pv_access_point_ids]
    return deprecated_access_points_ids

def delete_access_points(access_point_ids, profile):
    # Iterate over each access point ID and delete it
    for access_point_id in access_point_ids:
        aws_command = ['aws', 'efs', 'delete-access-point', '--access-point-id', access_point_id, '--profile', profile]
        subprocess.run(aws_command)

if __name__ == "__main__":

    # the filesystem id
    efs_filesystem_id = 'XXXXXX'
    # the profile
    profile = 'XXXXX'

    # Run the Kubectl Command to get pv info
    pv_info = get_pv_info()
    # Extract the PV access point id
    pv_access_point_ids = extract_pv_access_point_id(pv_info)
    # Print the PV access point ids and the number of PVs
    print("PV access point ids:")
    print(pv_access_point_ids)
    print("Number of PVs:", len(pv_access_point_ids))


    # Run the AWS command
    access_point_output = run_aws_command(efs_filesystem_id, profile)
    # Extract the access point path
    access_point_ids = extract_access_point_ids(access_point_output)
    # Print the access point ids and the number of EFS Access Points
    print("EFS Access Point IDs:")
    print(access_point_ids)
    print("Number of EFS Access Points:", len(access_point_ids))




    # Find unique paths
    Deprecated_access_point_ids = find_unique_ids(pv_access_point_ids, access_point_ids)
    print("Deprecated access point IDs:")
    print(Deprecated_access_point_ids)
    print("Number of Deprecated access point ids:", len(Deprecated_access_point_ids))
  

    delete_access_points(Deprecated_access_point_ids, profile)



