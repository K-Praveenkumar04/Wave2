#root = -b +/- square root... 
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
discriminant = (b * b) - (4 * a * c)
print (discriminant)
if discriminant > 0:
    realroot1 = (-b + math.sqrt(discriminant) / (2 * a))
    realroot2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("This equation has two real roots: " + str(realroot1) + " and " + str(realroot2))
elif discriminant == 0:
    realroot1 = realroot2 = -b / (2 * a)
    print("This equation has one real root: " + str(realroot1) + " and " + str(realroot2))
else:
    print("This equation has no real roots")