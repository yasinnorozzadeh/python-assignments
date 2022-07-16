import random
list=[]
len_n = int(input("input len of numbers in list : "))
while len_n != len(list) :
    numer_add = random.randint(0 , 31)
    if numer_add not in list:
        list.append(numer_add)
print(list)
