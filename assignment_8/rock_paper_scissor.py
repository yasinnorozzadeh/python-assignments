import random
game = ["paper", "scissor", "rock"]
score_players = {"computer": 0, "user": 0}
while True:
    computer = random.choice(game)
    user = int(input("1:Paper\t 2:Scissor\t 3:Rock\t 4:exit and score"))
    if computer == game[0] and user == 2 or computer == game[1] and user == 3 or computer == game[2] and user == 1:
        score_players["user"] += 1
        print("user get 1 point", score_players["user"])
    elif computer == game[0] and user == 3 or computer == game[1] and user == 1 or computer == game[2] and user == 2:
        score_players["computer"] += 1
        print("computer get 1 point" , score_players["computer"])
    elif user == 4:
        break
    else:
        print("equal")
if score_players["computer"] > score_players["user"]:
    print("computer win!!")
elif score_players["computer"] < score_players["user"]:
    print("user win!!")
else:
    print("equal !!")
