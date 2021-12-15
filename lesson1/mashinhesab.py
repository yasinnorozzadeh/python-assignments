import math 

result = ""

op = input('''+ , - , * , / , sin , cos , tan , radical
''' )

if op == "radical" or op == "sin" or op == "tan" or op == "cos":
    a = float(input("input number => "))
    if op == "sin":
        result = math.sin(a) 
    if op == "cos":
        result = math.cos(a)
    if op == "tan":
        result == math.tan(a)
    if op == "radical":
        result = math.sqrt(a)


else:
    b = float(input("input number 1 => "))
    c = float(input("input number 2 => "))
    if op == "+" :
        result = b + c

    elif op == "-" :
        result = b - c

    elif op == "*":
        result = b * c

    elif op == "/":
        result = b / c

print(result)
