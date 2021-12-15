w = float(input(''' input youre weight (kg)
'''))
h = float(input(''' input youre height (meter)
'''))
bmi = w / (h ** 2 )

if bmi < 25:
    print("1")
else:
    if 25 <= bmi >= 29.9:
        print("2")
    elif 30 <= bmi >= 34.9:
        print("3")
    else:
        print("4")
