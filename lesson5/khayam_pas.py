
n = int(input("input number : "))
kh_pas = [[None for i in range(n)] for i in range(n)] 
for i in range(n):
    kh_pas[i][0] = 1
    kh_pas[i][i] = 1
for i in range(2 , n):
    for j in range(1 , i):
        kh_pas[i][j] = kh_pas[i-1][j] + kh_pas[i-1][j-1]
for i in range(n):
    for j in range(i+1):
        print(kh_pas[i][j] ,end = "\t")
    print()
