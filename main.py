import random
import os
import time

def clear():
    os.system("clear")

def game_instructions():
    print("These are the instructions to the game rock paper scissors")
    print("Rock crushes scissors")
    print("Scissors cuts paper")
    print("Paper covers rock")
    print("Type help for help")

    print()
  


def rps():
    global name
    global win_lose_matrix
    global game_map 

    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
 
        print()

        inp = input("Enter your move ")
        if inp.lower() == "help":
            clear()
            game_instructions()
            continue
        
        elif inp.lower() == "rock":
            player_move = 0

        elif inp.lower() == "paper":
            player_move = 1

        elif inp.lower() == "scissors":
            player_move = 2

        else:
            clear()
            print("choose a valid option")
            game_instructions()
            continue
        print("Computer making a move")
        print()
        time.sleep(2)

        comp_move = random.randint(0, 2)
        print("Computer chooses ", game_map[comp_move].upper())

        winner = win_lose_matrix[player_move][comp_move]

        if winner == player_move:
            print(name, "WINS!!!")
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")
        print()
        time.sleep(2)
        clear()




if __name__ == "__main__":
    
    game_map = {0:"rock" , 1:"paper" ,2:"scissors"}

    win_lose_matrix = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
    name = input("Enter your name to play ")


while True:
    

    print("Hello",name,"Welcome to rock, paper scissors")
    print("Choose 1 to play the game ")
    print("Choose 2 to quit the game")
    print()
    try:
        choice = int(input("Enter a choice "))
    except ValueError:
        clear()
        print("That is not a valid number Try again")
        continue


    if choice == 1:
        rps()
    elif choice == 2:
        break

    else:
        print("Not a valid option. Choose either 1 or 2")


   
    

      

