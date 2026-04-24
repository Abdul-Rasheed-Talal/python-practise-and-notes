import math

def area_and_circumference(r):
    area = math.pi*r*r
    circumference = 2*math.pi*r
    return area , circumference

print(area_and_circumference(3))