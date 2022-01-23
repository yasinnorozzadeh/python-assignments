adad = int(input())
adad_fct = int(1)
if adad <= 1:
        print("no")
        exit()
def faktorial(adad_fct):      
    for i in range(2 , adad+1):
        adad_fct = adad_fct * i
        if adad_fct == adad :
            print(" _yas_ ")
            break
    if adad != adad_fct:
        print(" _no_ ")    
faktorial(adad_fct)
