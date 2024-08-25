import random
print('ROCK PAPER SCISSORS')
print("cases in the game are:")
print("Rock vs Paper then Paper wins")
print("Rock vs Scissors then Rock wins")
print("Paper vs Scissors then Scissor wins")
while True:
    print("Enter your choice ")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    choice = int(input("Enter your choice :"))
    while choice!=1 and choice!=2 and choice!=3:
        choice = int(input('valid choice to be entered'))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is ', choice_name)
    print('Now its Computers Turn....')
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    if (choice == 1 and comp_choice == 2):
        print('paper wins', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins', end="")
        result = 'Paper'
    if (choice == 1 and comp_choice == 3):
        print('Rock wins', end=" ")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins', end=" ")
        result = 'RocK'
    if (choice == 2 and comp_choice == 3):
        print('Scissors wins', end=" ")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins', end=" ")
        result = 'Rock'

    if result == 'DRAW':
        print("ITS A TIE")
    if result == choice_name:
        print("USER WINS")
    else:
        print("\n COMPUTER WINS")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("PLAYING DONE!")
