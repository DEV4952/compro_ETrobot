import math

r = int(input("Enter raduis: "))
h = int(input("Enter height: "))

def calCylinder(r, h):
    v = math.pi * (r ** 2) * h
    print("Cylinder volumn: " + str(v))
def calCone(r, h):
    v = (1 / 3) * math.pi * (r ** 2) * h
    print("Cone volumn: " + str(v))
def calSphere(r, h):
    v = (4 / 3) * math.pi * (r ** 3)
    print("Sphere volumn: " + str(v))

calCylinder(r, h)
calCone(r, h)
calSphere(r, h)