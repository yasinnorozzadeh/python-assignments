hour = int(input("Enter hours:\n"))
minute = int(input("Enter minutes:\n"))
second = int(input("Enter seconds:\n"))
if hour < 0 or minute < 0 or second < 0 :
    print("error")
else:
    time = (hour * 3600) + (minute * 60) + second
    print("second:", time)
