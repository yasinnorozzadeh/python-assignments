student_number = int(input("input student number as int =>"))
student_list = []
sum = 0
for i in range(student_number):
    sum1 = float(input("input student score : "))
    student_list.append(sum1)

for i in range(len(student_list)):
    sum += student_list[i]

average = sum / student_number

student_list.sort()
max = student_list[student_number-1]
min = student_list[0]
print("max score:" , max , "|" , "min score:" , min , "|" , "all average" ,  average)
