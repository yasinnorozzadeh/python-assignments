class Time:
    def __init__(self, second = None, minut = None, hour = None):
        self.h = hour
        self.m = minut
        self.s = second
    def sum_time(self, time2):
        Sum  = Time()
        self.time2 = time2
        Sum.s = self.s + time2.s
        Sum.m = self.m + time2.m
        Sum.h = self.h + time2.h
        r = True
        while r:
            if Sum.s >= 60:
                Sum.s -= 60
                Sum.m += 1
            elif Sum.m >= 60:
                Sum.m -= 60
                Sum.h += 1
            else:
                r = False
        return Sum
    def sub_time(self, time2):
        Sub = Time()
        self.time2 = time2
        Sub.s = self.s - time2.s
        Sub.m = self.m - time2.m
        Sub.h = self.h - time2.h
        r = True
        while r:
            if Sub.s < 0 :
                Sub.s += 60
                Sub.m -= 1
            elif Sub.m < 0 :
                Sub.m += 60
                Sub.h -= 1
            else:
                r = False
        return Sub
    def time_2_second(self, s, m, h):
        return int(s + (m * 60) + (h * 3600))
    def second_2_time(self, s):
        sec_2_time = Time()
        sec_2_time.s = s
        sec_2_time.m = 0
        sec_2_time.h = 0
        r = True
        while r:
            if sec_2_time.s >= 60:
                sec_2_time.s -= 60
                sec_2_time.m += 1
            elif sec_2_time.m >= 60:
                sec_2_time.m -= 60
                sec_2_time.h += 1
            else:
                r = False
        return sec_2_time
    def result(self):
        print(self.h, ":", self.m, ":", self.s)  
time = Time()
while True:
    op_time = int(input("1 => _sum_of_time\n2 => _sub_of_time\n3 => second_2_time\n4 => time_2_second\n5 => _exit_ \nenter number of operation_time:\t"))
    if op_time == 1 or op_time == 2:
        sec_first = int(input("enter secconds of time1:\t"))
        min_first = int(input("enter minutes of time1:\t"))
        hour_first = int(input("enter hours of time1:\t"))
        sec_second = int(input("enter secconds of time2:\t"))
        min_second = int(input("enter minutes of time2:\t"))
        hour_second =  int(input("enter hours of time2:\t"))
        time_first  = Time(sec_first, min_first, hour_first)
        time_second = Time(sec_second, min_second, hour_second)
        if op_time == 1:
            time_first.sum_time(time_second).result()
        if op_time == 2:
           time_first.sub_time(time_second).result()
    elif op_time == 3:
        time_third = int(input("enter seconds:\n"))
        time.second_2_time(time_third).result()
    elif op_time == 4:
        sec = int(input("enter secconds of time1:\t"))
        min = int(input("enter minutes of time1:\t"))
        hour= int(input("enter hours of time1:\t"))
        print("seconds:\t", time.time_2_second(sec, min, hour))
    elif op_time == 5:
        exit()
    else:
        print("select number of list")
