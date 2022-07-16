seconds = int(input("enter scondes for convert to hours:\n"))

if seconds == 0:
    print("error")
else:
    hours = int(seconds // 3600)
    seconds -= hours * 3600
    minutes = int(seconds // 60)
    seconds -= minutes * 60
    if hours >= 24:
        days = int(hours // 24)
        hours -= days * 24
    print("time:", days, ":", hours, ":", int(minutes), ":", int(seconds))
