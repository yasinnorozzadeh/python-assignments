number1 = int(input('''input number1 for tryangel =>
'''))
number2 = int(input('''input number2 for tryangel =>
'''))
number3 = int(input('''input number3 for tryangel =>
'''))
if number1 == 0 and number2 == 0 and number3 == 0:
    print("f")
else:
    if number1 + number2 >= number3 or number1 + number3 >= number2 or number2 + number3 >= number1 :
        print("True")
    else:
        print("f")
