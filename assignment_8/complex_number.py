def Sum():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    sum = {"numerator": 0, "Denominator": 0}
    sum["numerator"] = d1["numerator"] + d2["numerator"]
    sum["Denominator"] = d1["Denominator"] + d2["Denominator"]
    return sum
def Sub():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    sub = {}
    sub["numerator"] = d1["numerator"] - d2["numerator"]
    sub["Denominator"] = d1["Denominator"] - d2["Denominator"]
    return sub
def Mul():
    d1 = {"numerator": int(input("numerator1:\t")), "Denominator": int(input("Denominator1:\t"))}
    d2 = {"numerator": int(input("numerator2:\t")), "Denominator": int(input("Denominator2:\t"))}
    mul = {}
    mul["numerator"] = (d1["numerator"] * d2["numerator"]) - (d1["Denominator"] * d2["Denominator"])
    mul["Denominator"] = (d1["Denominator"] * d2["numerator"]) + (d1["numerator"] * d2["Denominator"])
    return mul
while True:
    op = int(input("1: sum\n2: sub\n3: mul\n4: exit\nenter operation:\t"))
    if op == 1:
        sum = Sum()
        print("sum:", sum["numerator"], sum["Denominator"])
    elif op == 2:
        sub = Sub()
        print("sub:", sub["numerator"], sub["Denominator"])
    elif op == 3:
        mul = Mul()
        print("mul:", mul["numerator"], mul["Denominator"])
    elif op == 4:
        exit()
    else:
        print("select number from list")