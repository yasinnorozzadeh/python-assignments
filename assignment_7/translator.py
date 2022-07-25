import pyfiglet
WORDS_LIST = []

def Load():
    my_file = open("words.txt", "r")
    words = my_file.read().lower().split("\n")
    for i in range(1, len(words), 2):
        dict = {}
        dict["english"] = words[i-1]
        dict["persian"] = words[i]
        WORDS_LIST.append(dict)

    f = pyfiglet.figlet_format("yasin dictionary", font = "digital" )
    print(f)
def Add():
    f = pyfiglet.figlet_format("add word", font = "isometric1" )
    while True:
        print(f)
        new_english_word = input("enter english word:\n")
        new_persian_word = input("enter persian word:\n")
        new_dict_words = {}
        for i in range(len(WORDS_LIST)):
            new_dict_words["english"] = new_english_word
            new_dict_words["persian"] = new_persian_word
            WORDS_LIST.append(new_dict_words)
        repeat = input("do you want to translate agane?(Y/N)")
        if repeat == "N" or repeat == "n":
            break
def Save():
    f = open("words.txt", "w")
    for i in range(len(WORDS_LIST)):
        save_data = WORDS_LIST[i]['english'] + '\n' + WORDS_LIST[i]['persian']
        f.write(str(save_data))
        if i != len(WORDS_LIST) -1:
            f.write('\n')
    f.close()
def Choice():
    choice = int(input(" 1.add word\n 2.english_2_persian\n 3.persian_2_english\n 4.save_and_exit\n"))
    if choice == 1:
        Add()
    elif choice == 2:
        Engelish_2_Persian()
    elif choice == 3:
        Persian_2_English()
    elif choice == 4:
        font = pyfiglet.figlet_format("save", font = "doh" )
        print(font)
        Save()
        exit()
    else :
        print("number is not in the list, please enter the number\n")
def Persian_2_English():
    while True:
        search_persian_word = input('enter persian word:\n').lower().split(" ")
        for s in range(len(search_persian_word)):
            for i in range(len(WORDS_LIST)):
                if search_persian_word[s] == WORDS_LIST[i]['persian']:
                    print(WORDS_LIST[i]['english'], end=" ")
                    break
        print()
        repeat = input("do you want to translate agane?(Y/N)")
        if repeat == "N" or repeat == "n":
            break
def Engelish_2_Persian():
    while True:
        search_english_word = input('enter english word:').lower().split(".")
        for j in range(len(search_english_word)):
            search_english_word = search_english_word[j].split(" ")
            for s in range(len(search_english_word)):    
                for i in range(len(WORDS_LIST)):
                    if search_english_word[s] == WORDS_LIST[i]['english']:
                        print(WORDS_LIST[i]['persian'], end=" ")
                        break
        print()
        repeat = input("do you want to translate agane?(Y/N)")
        if repeat == "N" or repeat == "n":
            break

Load()
while True:
    Choice()
    Save()
