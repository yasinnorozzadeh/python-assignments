import random
import time
from colored import fg
from termcolor import colored

start_time = time.time()
user = int(input('exit = 0 | 1 player = 1 | 2 players = 2\ninput number of options:'))
if user == 0:
    exit()
nut_user = int(input("X = 1\tO = 2:\n"))
game_board = [['_ ', '_ ', '_ '],
              ['_ ', '_ ', '_ '],
              ['_ ', '_ ', '_ ']]
nut = [colored("X ", "red"), colored("O ", "blue")]

def Game_board():
    for i in range(3):
        for j in range(3):
            print(game_board[i][j] , fg(3), end="")
        print()

def Nut(nut_user):
    if nut_user == 1:
        player1 = nut[0]
        player2 = nut[1]
    elif nut_user == 2:
        player1 = nut[1]
        player2 = nut[0]
    return player1, player2
player1, player2 = Nut(nut_user)
def Win_condition():
    for r in range(3):
        s1r = 0
        s2r = 0
        s1c = 0
        s2c = 0
        for c in range(3):
            if game_board[r][c] == player1:
                s1r += 1
            elif game_board[r][c] == player2:
                s2r += 1
            elif game_board[c][r] == player1:
                s1c += 1
            elif game_board[c][r] == player2:
                s2c += 1
            if s1r == 3 or s1c == 3:
                print("palyer one wins", "\nTime out is:", time.time() - start_time)
                exit()
            elif s2r == 3 or s2c == 3:
                print("player two wins", "\nTime out is:", time.time() - start_time)
                exit()
    if game_board[0][0] == player1 and game_board[1][1] == player1 and game_board[2][2] == player1 or game_board[0][2] == player1 and game_board[1][1] == player1 and game_board[2][0] == player1:
        print("player one wins", "\nTime out is:", time.time() - start_time)
        exit()
    elif game_board[0][0] == player2 and game_board[1][1] == player2 and game_board[2][2] == player2 or game_board[2][0] == player2 and game_board[1][1] == player2 and game_board[0][2] == player2:
        print("player two wins", "\nTime out is:", time.time() - start_time)
        exit()

def Two_player():
    print("player1 nut is:", player1, "player2 nut is:", player2)
    while True:
        row = int(input("enter your row:\n"))
        col = int(input("enter your column:\n"))
        selection_turn_player = 0
        if 0 <= row < 3 and 0 <= col < 3 and selection_turn_player == 0:
            if game_board[row][col] == "_ ":
                game_board[row][col] = player1
                selection_turn_player += 1
            else :
                print("it is not empty")
            Game_board()
            Win_condition()
        elif 0 <= row < 3 and 0 <= col < 3 and selection_turn_player == 1:
            if game_board[row][col] == "_ ":
                game_board[row][col] = player2
                selection_turn_player -= 1
            else :
                print("it is not empty")
            Game_board()
            Win_condition()
        else :
            print("Enter row and columns between 0 and 2")

def One_player():
    selection_turn_player = 0
    print("player1 nut is:", player1, "player2 nut is:", player2)
    while True:
        if selection_turn_player == 0:

            row = int(input("enter your row:\n"))
            col = int(input("enter your column:\n"))
            if 0 <= row < 3 and 0 <= col < 3:
                if game_board[row][col] == "_ ":
                    game_board[row][col] = player1
                    selection_turn_player += 1
        Win_condition()
        if selection_turn_player == 1:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if 0 <= row < 3 and 0 <= col < 3:
                if game_board[row][col] == "_ ":
                    game_board[row][col] = player2
                    selection_turn_player -= 1
        Game_board()
        Win_condition()
if user == 1:
    One_player()
elif user == 2:
    Two_player()
