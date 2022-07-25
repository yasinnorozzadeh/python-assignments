seconds = int(input("enter scondes for convert to hours:\n"))

if seconds == 0:
    print("error")
else:
    hours = int(seconds // 3600)
    seconds -= hours * 3600
    minutes = int(seconds // 60)
    seconds -= minutes * 60
    print("time:", hours, ":", int(minutes), ":", int(seconds))
