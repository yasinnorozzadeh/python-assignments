from pyfiglet import Figlet
import qrcode

def Show_List():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
def Load():
    F = open("databace.txt", "r")
    data = F.read()
    product_list = data.split("\n")
    for i in range(len(product_list)):
        product_info = product_list[i].split(",")
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = int(product_info[3])
        PRODUCTS.append(mydict)
    print("welcome")
    f = Figlet(font="standard")
    print(f.renderText("Yasin Store #_#"))
def Add():
    while True:
        new = {}
        new["id"] = input("Enter id:\n")
        new["name"] = input("Enter name:\n")
        new["price"] = input("Enter price:\n")
        new["count"] = input("Enter count:\n")
        PRODUCTS.append(new)
        true_repeat = input("do you add enother product?(Y/N):\n")
        if true_repeat == "n" or true_repeat == "N":
            break
def Edit():
    while True:
        edit_from_name = input("Enter name product:\n")
        for i in range(len(PRODUCTS)):
            if edit_from_name == PRODUCTS[i]["name"]:
                edit_item = int(input('1.Edit id\n 2.Edit name\n 3.Edit price\n 4.Edit count\nEnter number:'))
                if edit_item == 1 :
                    PRODUCTS[i]["id"] = input("Enter new id:\n")
                elif edit_item == 2 :
                    PRODUCTS[i]["name"] = input("Enter new name:\n")
                elif edit_item == 3 :
                    PRODUCTS[i]["price"] = input("Enter new pice:\n")
                elif edit_item == 4 :
                    PRODUCTS[i]["count"] = input("Enter new count:\n")
        edit_repeat = input('do you edit enother product(Y/N):')
        if edit_repeat == 'n' or 'N':
            break
def Delet():
    while True:
        id_or_name_deleting = input("enter id or name for delet product:\n")
        for i in range(len(PRODUCTS)):
            if id_or_name_deleting == PRODUCTS[i]["id"]:
                PRODUCTS.remove(PRODUCTS[i])
            elif id_or_name_deleting == PRODUCTS[i]["name"]:
                PRODUCTS.remove(PRODUCTS[i])
        repeat_deleting = input("do you repeat deletting?(Y/N)\n")
        if repeat_deleting == "n" or "N":
            break
def Search():
    while True:
        searching_id_or_name = input("enter id or name product:\n")
        for i in range(len(PRODUCTS)):
            if searching_id_or_name == PRODUCTS[i]["id"]:
                print(PRODUCTS[i])
            elif searching_id_or_name == PRODUCTS[i]["name"]:
                print(PRODUCTS[i])
        repeat_searching = input('search enother product(Y/N):')
        if repeat_searching == 'n' or 'N':
            break
def Buy():
    while True:
        id_for_buy = input("enter id product for buy:\n")
        number = int(input("how many product want?\n"))
        for i in range(len(PRODUCTS)):
            if id_for_buy == PRODUCTS[i]["id"]:
                if PRODUCTS[i]["count"] >= number:
                    PRODUCTS[i]["count"] = int(PRODUCTS[i]["count"]) - number
                else:
                    print(int(PRODUCTS[i]["count"]))
                    
        repeat_buy = input("do you buy enother product?(Y/N)\n")
        if repeat_buy == "n" or "N":
            break
def Qrcode():
    while True:
        id_qurcode = input("Enter id for qurcode:\n")
        for i in range(len(PRODUCTS)):
            if id_qurcode == PRODUCTS[i]["id"]:
                img = qrcode.make(PRODUCTS[i]['id'])
                img.save(PRODUCTS[i]['id'] + '.png')
            repeat_qurcode = input("do you make new qurcode?(Y/N)")
        if repeat_qurcode == 'n' or 'N':
            break
def choice():
    choice = int(input(" 1.Add\n 2.Edit\n 3.Delet\n 4.search\n 5.Show List\n 6.Buy\n 7.Qrcode\n 8.Exit\nPlease choose a number:\n"))
    if choice == 1:
        Add()
    elif choice == 2:
        Edit()
    elif choice == 3:
        Delet()
    elif choice == 4:
        Search()
    elif choice == 5:
        Show_List()
    elif choice == 6:
        Buy()
    elif choice == 7:
        Qrcode()
    elif choice == 8:
        f = Figlet(font = 'standard')
        print(f.renderText('goodbye'))
        exit()
def Register_in_list():
    f = open("databace.txt", "w")
    for i in range(len(PRODUCTS)):
        f.write(PRODUCTS[i]['id'])
        f.write(',')
        f.write(PRODUCTS[i]['name'])
        f.write(',')
        f.write(PRODUCTS[i]['price'])
        f.write(',')
        f.write(str(PRODUCTS[i]['count']))
        if i != len(PRODUCTS) -1:
            f.write('\n')
PRODUCTS = []
Load()
Show_List()
while True:
    choice()
    Register_in_list()
