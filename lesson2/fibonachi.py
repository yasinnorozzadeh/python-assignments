n = int(input('input number of fibonachi list => '))
fibonachi = []
for f in range(n):
    if f < 2 :
        fibonachi.append(1)   
    else:
        fibo = fibonachi[f-1] + fibonachi[f-2]
        fibonachi.append(fibo)
print(fibonachi)
