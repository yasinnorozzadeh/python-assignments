n = int(input("input hight snake :"))
i = 0
if n <= 5 :
    print("not draw snake")
else:
    if n % 2 == 1:
        print("*" , end="")
        for j in range(n):
            i += 2
            if n <= i :
                exit()
            print("#" , end = "" )
            if n <= i :
                exit()
            print("*" , end = "")
    else:
        for k in range(n):
            i += 2
            if n < i :
                exit()
            print("#" , end = "")
            if n < i :
                exit()
            print("*" , end = "")
