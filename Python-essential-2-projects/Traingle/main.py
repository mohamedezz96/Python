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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__traingle_points = [vertice1, vertice2, vertice3]
        


    def perimeter(self):
        dimension_1 = self.__traingle_points[0].distance_from_point(self.__traingle_points[1])
        dimension_2 = self.__traingle_points[0].distance_from_point(self.__traingle_points[2])
        dimension_3 = self.__traingle_points[1].distance_from_point(self.__traingle_points[2])
        paremeter = dimension_1 + dimension_2 + dimension_3
        return paremeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    
