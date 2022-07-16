import random
computer_tas = random.randint(1 , 6)
print(computer_tas)
while computer_tas == 6:
    computer_tas = random.randint(1 , 6)
    print("bonus : " , computer_tas)
