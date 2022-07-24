def Sum():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    sum = {}
    if d1["Denominator"] == d2["Denominator"]:
        sum["numerator"] = d1["numerator"] + d2["numerator"]
        sum["Denominator"] = d1["Denominator"]
    else:
        sum["Denominator"] = d1["Denominator"] * d2["Denominator"]
        sum["numerator"] = (d1["numerator"] * d2["Denominator"]) + (d1["Denominator"] * d2["numerator"])
    return sum
def Sub():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    sub = {}
    if d1["Denominator"] == d2["Denominator"]:
        sub["numerator"] = d1["numerator"] - d2["numerator"]
        sub["Denominator"] = d1["Denominator"]
    else:
        sub["numerator"] = (d1["numerator"] * d2["Denominator"]) - (d1["Denominator"] * d2["numerator"])
        sub["Denominator"] = d1["Denominator"] * d2["Denominator"]
    return sub
def Mul():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    mul = {}
    mul["numerator"] = d1["numerator"] * d2["numerator"]
    mul["Denominator"] = d1["Denominator"] * d2["Denominator"]
    return mul
def Div():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    div = {}
    if d2["numerator"] != 0 and d2["Denominator"] != 0:
        div["numerator"] = d1["numerator"] * d2["Denominator"]
        div["Denominator"] = d1["Denominator"] * d2["numerator"]
        return div
    else:
        e = 1
        return e
    

while True:
    op = int(input("1: sum\n2: sub\n3: mul\n4: div\n5: exit\nenter opration:\t"))
    if op == 1:
        sum = Sum()
        print("sum:", sum["numerator"], "/", sum["Denominator"])
    elif op == 2:
        sub = Sub()
        print("sub:", sub["numerator"], "/", sub["Denominator"])
    elif op == 3:
        mul = Mul()
        print("mul:", mul["numerator"], "/", mul["Denominator"])
    elif op == 4:
        div = Div()
        if div != 1:
            print("div:", div["numerator"], "/", div["Denominator"])
        else:
            print("no answer!")
    elif op == 5:
        exit()
    else:
        print("select number from list")