sum=0
while True:
    user_number = input("__exit__ and __sum__ = exit\nEnter number:")
    if user_number == "exit":
        if sum == 0:
            print("sum:", sum)
            exit()
        break
    else:
        sum += float(user_number)
    print("sum : ", sum)
print("sum : ", sum)
