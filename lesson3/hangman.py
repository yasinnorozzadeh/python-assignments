import random
true_ch = []
print("youre score : 10")
score = 10
words = ["Book" , "Tree" , "Python" , "Bag" , "Umbrella" , "Dog" , "Clock" , "Engineer" , "Toothpast" , "Shirmoz"]
word = random.choice(words)
word = word.lower()
print ("_ " * len(word) , ":")
test = -1
while not score <= 0:
    user_charater = input("input youre character : ").lower()
    if user_charater in word :
        true_ch.append(user_charater)
        print("youre input true character\n")
    else:
        score -= 1
        print("no |" , "youre score: " , score)
    for i in range(len(word)):
        if word[i] in true_ch:
            print(word[i],end="") 
        else:
            print("_ ",end="")
        test += 1
    if len(word) == len(true_ch) :
        print("|" , "__ you win __", "|", word)
        exit()
print("| youre lose |" , word)
