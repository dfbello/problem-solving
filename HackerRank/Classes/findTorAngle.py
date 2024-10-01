# Classes - find the torsional angle

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x_coord = self.x - no.x
        y_coord = self.y - no.y
        z_coord = self.z - no.z
        
        res = Points(x_coord, y_coord, z_coord)
        return res

    def dot(self, no):
        res = self.x * no.x + self.y * no.y + self.z * no.z
        return res

    def cross(self, no):
        x_coord = self.y * no.z - self.z * no.y
        y_coord = self.x * no.z - self.z * no.x
        z_coord = self.x * no.y - self.y * no.x
        
        res = Points(x_coord, y_coord, z_coord)
        return res
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()

    with open("./input.txt", "r") as file:

	    for i in range(4):
	        a = list(map(float, file.readline().split()))
	        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
