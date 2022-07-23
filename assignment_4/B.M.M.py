adad1 = int(input("input numbber1 =>"))
adad2 = int(input("input numbber2 =>"))
if adad1 == 1 or adad2 == 1:
    print("not print b.m.m")
    exit()
else:
    if adad1 > adad2:
        max  = adad1
        min = adad2
    else:
        max = adad2
        min = adad1
for i in range(1 ,max+1):
    if adad1 % i == 0 and adad2 % i == 0:
        BMM = i
print("B.M.M =>" , BMM)
