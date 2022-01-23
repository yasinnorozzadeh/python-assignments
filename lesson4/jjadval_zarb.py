n = int(input("input :"))
m = int(input("input :"))
def jadval():
    for i in range(1, n+1):
        for j in range (1 , m+1):
            print(i *j , end= "\t")
        if j == m:
            print()
jadval()
