name = input(''' input youre name =>
''')
family = input(''' input your family
''')

Lesson_1 = float(input(''' input Score Lesson 1 =>
'''))
Lesson_2 = float(input(''' input Score Lesson 2 =>
'''))
Lesson_3 = float(input(''' input Score Lesson 3 =>
'''))

sum =Lesson_1 + Lesson_2 + Lesson_3
average = sum / 3


if average <= 12 :
    print("fail")
else:
    if 12 <= average <= 17:
        print ("normal")
    else:
        print("great")

        
