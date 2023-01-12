import random as r

while True:
    user_action=input("enter a choice(rock=r,paper=p,scissors=s): ")
    possible_actions=["r","p","s"]
    computer_action=r.choice(possible_actions)                      #random use insted to random (random use for selection by computer)
    print(f'\nyou chose {user_action},computer chose {computer_action}.\n')   #f=format method for list.it use for connect variable to print

    if user_action== computer_action:
        print(f"Both players selested {user_action}.it's a tie!🤝")
    elif user_action =="r":
        if computer_action=="s":
            print("Rock smasthes scissors! you Win!🥇")
        else:
            print("Paper covers rock! you lose.👎")
    elif user_action=="p":
        if computer_action == "s":
            print("you Lose👎.Scissor cuts paper.")
        else:
            print("you Wins🥇,Paper covers Rock!")
    elif user_action == "s":
        if computer_action == "r":
            print("you Lose👎.Rock smashes Scissors!.")
        else:
            print("you wins🥇.Scissor cuts paper!.")
    else:
        print("Invalid input!🤦")
    play_again=input("Whether you want to play again?(y/n) : ")
    if play_again.lower()!="y":
        break

