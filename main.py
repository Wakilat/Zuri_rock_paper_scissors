import random

play = True
while play == True:
    game = input("Do you wish to play? y/n \n").lower()
    if (game == 'y'):
        print("R for rock\nP for paper\nS for scissors")
        player = input("Make a selection between R, S, P to play\n")
        play = "true"
        select = ["Rock", "Paper", "Scissors"]
        choices = ['R', 'P', 'S']
        CPU = random.choice(choices)
        if CPU == player:
            print(f"it's a tie!!! The computer made the same choice,{CPU}, as you")
            play = True
        elif CPU == 'R'and player == 'S':
            print(f"CPU ({select[0]}) : Player ({select[2]})")
            print(f"The computer wins this round with {CPU}: Rock which smashes {player}: Scissors")
            play = False
        elif CPU == 'P' and player == 'R':
            print(f"CPU ({select[1]}) : Player ({select[0]})")
            print(f"The computer wins this round with {CPU}: Paper which covers {player}: Rock")
            play = False
        elif CPU == 'S' and player == 'P':
            print(f"CPU ({select[2]}) : Player ({select[1]})")
            print(f"The computer wins this round with {CPU}: Scissors which can cut through {player}: paper")
            play = False
        elif CPU == 'R' and player == 'P':
            print(f"CPU ({select[0]}) : Player ({select[1]})")
            print(f"Paper covers rock! You win with {player}: Paper")
            play = False
        elif CPU == 'P' and player == 'S':
            print(f"CPU ({select[1]}) : Player ({select[2]})")
            print("Scissors cuts paper! You win with {player}: Scissors")
            play = False
        elif CPU == 'S' and player == 'R':
            print(f"CPU ({select[2]}) : Player ({select[0]})")
            print(f"Rock smashes Scissors! You win!!!")
            play = False
        else:
            print("Invalid option")
            play = True
    
    elif (game == 'n'):
        print("Have a nice day!!!\n")
        break

    else:
        print("Invalid selection")
