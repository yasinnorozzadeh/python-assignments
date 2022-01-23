import random
list=[]
tedad = int(input("input number of numbers in list : "))
while tedad == len(list) :
    s = random.randint(0 , 31)
    if s not in list:
       list.append(s)
print( list )
