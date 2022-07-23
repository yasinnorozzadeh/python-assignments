def Sum_time():
    time1 = {}
    time1["s"] = int(input("enter second time1:\t"))
    time1["m"] = int(input("enter minute time1:\t"))
    time1["h"] = int(input("enter hour time1:\t"))
    time2 = {}
    time2["s"] = int(input("enter second time2:\t"))
    time2["m"] = int(input("enter minute time2:\t"))
    time2["h"] = int(input("enter hour time2:\t"))
    sum = {}
    sum["s"] = time1["s"] + time2["s"]
    sum["m"] = time1["m"] + time2["m"]
    sum["h"] = time1["h"] + time2["h"]
    while True:
        if sum["s"] >= 60:
            sum["s"] -= 60
            sum["m"] += 1
        elif sum["m"] >= 60:
            sum["m"] -= 60
            sum["h"] += 1
        else:
            break
    return sum

def Sub_time():
    time1 = {}
    time1["s"] = int(input("enter second time1:\t"))
    time1["m"] = int(input("enter minute time1:\t"))
    time1["h"] = int(input("enter hour time1:\t"))
    time2 = {}
    time2["s"] = int(input("enter second time2:\t"))
    time2["m"] = int(input("enter minute time2:\t"))
    time2["h"] = int(input("enter hour time2:\t"))
    sub = {}
    while True:
        if time2["s"] > time1["s"]:
            time1["m"] -= 1
            time1["s"] += 60
        elif time2["m"] > time1["m"]:
            time1["h"] -= 1
            time1["m"] += 60
        else:
            break
    sub["s"] = time1["s"] - time2["s"]
    sub["m"] = time1["m"] - time2["m"]
    sub["h"] = time1["h"] - time2["h"]
    return sub

def Second_2_time():
    seconds = int(input("enter seconds:\t"))
    s_2_t = {}
    s_2_t["s"] = seconds
    s_2_t["m"] = 0
    s_2_t["h"] = 0
    while True:
        if s_2_t["s"] >= 60:
            s_2_t["s"] -= 60
            s_2_t["m"] += 1
        elif s_2_t["m"] >= 60:
            s_2_t["m"] -= 60
            s_2_t["h"] += 1
        else:
            break
    return s_2_t

def Time_2_second():
    t_2_s = {}
    t_2_s['s'] = int(input('enter second:\t'))
    t_2_s['m'] = int(input('enter minute:\t'))
    t_2_s['h'] = int(input('enter hour:\t'))

    return t_2_s['s'] + (t_2_s['m'] * 60) + (t_2_s['h'] * 3600)

while True:
    op = int(input("1:Sum_time\t 2:Sub_time\t 3:second_2_time\t 4:time_2_second\t -1:_exit_\nenter operation:\n"))
    if op == 1:
        sum = Sum_time()
        print("time:\t", sum["h"], ":", sum["m"], ":", sum["s"])
    elif op == 2:
        sub = Sub_time()
        print("time:\t", sub["h"], ":", sub["m"], ":", sub["s"])
    elif op == 3:
        s_2_t = Second_2_time()
        print("time:\t", s_2_t["h"], ":", s_2_t["m"], ":", s_2_t["s"])
    elif op == 4:
        print("second:\t", Time_2_second())
    elif op == -1:
        exit()
    else:
        print("select another number:\n")