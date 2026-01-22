import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        distance = dist(self.__x,self.__y,x,y)
        return distance

    def distance_from_point(self, point):
        distance = dist(self.__x, self.__y,point.__x, point.__y)
        return distance



point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
    
