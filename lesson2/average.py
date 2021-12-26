student_number = int(input("input student number as int =>"))
student_list = []
sum = 0
for i in range(student_number):
    sum1 = float(input("input student score : "))
    student_list.append(sum1)
    sum = sum + sum1
student_list.sort()
average = sum1 / student_number
max = student_list[student_number-1]
min = student_list[0]
print("max average:" , max , "|" , "min average:" , min , "|" , "all average" ,  average)
