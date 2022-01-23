import random
true_ch = []
print("youre score : 10")
joon = 10
words = ["Book" , "Tree" , "Python" , "Bag" , "Umbrella" , "Dog" , "Clock" , "Engineer" , "Toothpast" , "Shirmoz"]
word = random.choice(words)
word = word.lower()
print ("_ " * len(word) , ":")
test = -1
while not joon == 1:
    user_charater = input("  | input youre character : ")
    if user_charater in word :
        true_ch.append(user_charater)
        print("youre input true character")
    else:
        joon -= 1
        print("no |" , "youre score:" , joon)
    for i in range(len(word)):
        if word[i] in true_ch:
            print(word[i],end="") 
        else:
            print("_ ",end="")
        test += 1
    if len(word) == len(true_ch) :
        print("|" , word , "|" , "__ you win __")
        exit()
print("| youre lose |" , word)
