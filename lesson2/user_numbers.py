sum_list_user = 0
while True:
    user_input = int(input("__exit__ = -1       input number : "))
    if user_input >= 0 :
        sum_list_user += user_input
        print("sum numbers :" , sum_list_user )
    else:
        print("_____exit______")
        break
