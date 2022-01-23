list1 = []
sort = []
tedad = int(input("input numer numbers:"))
if tedad != 0:
    for i in range(tedad):
        list1_append = int(input("exit = 0 , input numbers:"))
        if list1_append == 0:
            break
        list1.append(list1_append)
    for i in range(len(list1)):
        if list1[i] < list1[i+1] :
            sort.append("sort :)")
        else:
            sort.append("dont sort!!")
        if "dont sort!!" in sort :
            print("dont sort!!")
            exit()
        else:
            print("sort :)")
            exit()
else:
    print("!! dont sort becuz for sort requires 2 numbers !!")