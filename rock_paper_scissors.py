import random

list1  = ["r","p","s"]

gamer_points =0
computer_points=0

number_of_choices = 5

def scrore_check(gamer_points,computer_points):
    if gamer_points> computer_points:
        print("you won the game")
    else:
        print("computer won the game")


def new_game():
    print("do you want to continue the game")
    option = input("please enter 'Y' for continue 'E' for exit")
    if option.upper() == 'Y':
        rock_paper_scissors_game(list1, number_of_choices)
    elif option.upper() == 'E':
        exit

def rock_paper_scissors_game(options, number):
    #print("please enter a r for rock , p for paper and 's' for scissors ")
    for i in range(number):
        gamer_choice = input("please enter a r for rock , p for paper and 's' for scissors ")
        if gamer_choice.lower() not in options:
            print("please enter 'r' or 's' or 'p' only ")
            i = i - 1
            continue
        computer_choice = random.choice(options)
        print("computer choice {}".format(computer_choice))

        if (gamer_choice == 'r' and computer_choice =='p') or (gamer_choice == 'p' and computer_choice =='s') or (gamer_choice == 's' and computer_choice =='r'):
            global gamer_points
            gamer_points += 1
        else:
            global computer_points
            computer_points += 1

    scrore_check(gamer_points,computer_points)
    new_game()


rock_paper_scissors_game(list1, number_of_choices)


