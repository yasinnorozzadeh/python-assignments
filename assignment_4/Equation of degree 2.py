from math import sqrt
a = int(input("input number :"))
b = int(input("input number :"))
c = int(input("input number :"))
mohasebe = b ** 2 - 4*(a * c)
if mohasebe == 0:
    x = -b - sqrt(mohasebe)
    print(x)
elif mohasebe > 0:
    x1 = (-b + sqrt(mohasebe)) / (2 * a)
    x2 = (-b - sqrt(mohasebe)) / (2 * a)
    print(x1 , x2)
else:
    print("no answer")
