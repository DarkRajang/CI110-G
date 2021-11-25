import random
import time

# Global Variables
# Dice Number
dice = [0, 0, 0, 0]
# Dice Display
die = ['', '', '', '']
# User input

a = 'yes'
# Game Number
g = 1
# User Wins
uw = 0
# Computer Wins
cw = 0
# Ties
t = 0

# Die number

# Range 0-1 is the users and range 2-3 are the computers
while a.lower() == 'yes' or a.lower() == 'y':
    # clear screen
    print('\n' * 100)
    # Game Number
    print("Game:", g)
    # Rolling dice
    print('Rolling Dice', end='')
    for i in range(3):
        time.sleep(1)
        print('.', end='')

    print()


# Storing how each die is Displayed
    for i in range(4):
        dice[i] = random.randint(1, 6)

        if dice[i] == 1:
            die[i] = "|   |\n| * |\n|   |"
        elif dice[i] == 2:
            die[i] = "|*  |\n|   |\n|  *|"
        elif dice[i] == 3:
            die[i] = "|*  |\n| * |\n|  *|"
        elif dice[i] == 4:
            die[i] = "|* *|\n|   |\n|* *|"
        elif dice[i] == 5:
            die[i] = "|* *|\n| * |\n|* *|"
        else:
            die[i] = "|* *|\n|* *|\n|* *|"

    # Score
    us = dice[0] + dice[1]
    cs = dice[2] + dice[3]

    # Players Dice
    print("Your Dice: \n{}\n\n{}\nScore: {}\n".format(die[0], die[1], us))

    # Computers Dice
    print('Rolling Dice Again', end='')
    for i in range(3):
        time.sleep(1)
        print('.', end='')
    print()
    print("Computers Dice: \n{}\n\n{}\nScore: {}\n".format(die[2], die[3], cs))

    g += 1

    # Who Wins
    if us > cs:
        uw += 1
        print('You win!\n')

    elif cs > us:
        cw += 1
        print('You lose!\n')

    else:
        t += 1
        print("You Tie!\n")

    print('Number of Ties: ', t)
    print("Your wins:", uw)
    print("Computer wins:", cw)

    a = input('Roll Again (y or n)? ')
