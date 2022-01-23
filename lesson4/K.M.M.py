adad1 = int(input("input numbber1 =>"))
adad2 = int(input("input numbber2 =>"))
if adad1 > adad2:
    max  = adad1
    min = adad2
else:
    max = adad2
    min = adad1
if max % min == 0:
    print(max)
    exit()
else:
    for i in range(max , (adad1*adad2)+1):
        if i % adad1 == 0 and i % adad2 == 0:
            KMM = i
print("K.M.M =>" , KMM)
