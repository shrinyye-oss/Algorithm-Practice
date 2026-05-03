from math import sqrt
s1 = float(input("Sidelengthofatriangle（sl):"))
s2 = float(input("Side length of a triangle (s2):"))
s3 = float(input("Side length of a triangle (s3):"))
s = (s1 + s2 + s3) / 2
area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("Area:", area)
