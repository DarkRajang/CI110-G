import time
from Die import Die


class Game:
    def __init__(self, nd=2, g=1, uw=0, cw=0, t=0):
        # Number of dice
        self.numdice = nd
        self.games = g
        self.userwins = uw
        self.compwins = cw
        self.ties = t
        self.ui = 'yes'

        self.dicePicker()
        self.main()

    def score(self):
        # Checking who won and increasing the score acordingly
        print()
        if self.ps > self.cs:
            self.userwins += 1
            print("You win!")

        elif self.ps < self.cs:
            self.compwins += 1
            print("You lose!")

        elif self.ps == self.cs:
            self.ties += 1
            print("You tie")

        print()

    # Returning the score
    def getScore(self):
        return self.userwins, self.compwins, self.ties

    def main(self):

        while self.ui.lower() == "yes" or self.ui.lower() == "y":
            # displaying the start message
            self.starMsg()
            # Genearting the dice
            self.diceGen()
            # Rolling the dice and displaying them to thes user
            self.rolling()
            # Calculting the score and displaying them to the user
            self.score()

            time.sleep(2)

            print(F"Number of ties: {self.ties}"
                  + F"\nYour wins: {self.userwins}"
                  + F"\nYour lose: {self.compwins}\n"
                  )

            # Seeing if the user wants to play again
            self.ui = input("Would you like to play again (Y/N)")

        print("Goodbye")

    def starMsg(self):
        # Clearing the screen
        if self.games != 1:
            print("\n" * 100)
        # Game Number
        print("Game:", self.games)
        # Rolling dice
        print('Rolling Dice', end='')
        for i in range(3):
            time.sleep(1)
            print('.', end='')
        print()

    # How many dice would are in the game
    def dicePicker(self):
        ui =\
            eval(input("How many dice would you like both parties to have?\n"))
        self.numdice = ui

        print()

    def rolling(self):
        self.ps = 0
        self.cs = 0

        # Displaying the players dice and score
        print('Your Dice: \n')

        for i in range(self.numdice):
            print('{}\n'.format(self.playerDice[i].getFace()))
            self.ps += self.playerDice[i].getValue()
        print("Your score : {}\n".format(self.ps))

        print('Rolling Dice Again', end='')
        for i in range(3):
            time.sleep(1)
            print('.', end='')

        print()

        # Displying the computesr dice
        print('Computers Dice: \n')

        for i in range(self.numdice):
            print('{}\n'.format(self.comDice[i].getFace()))
            self.cs += self.comDice[i].getValue()

        print("Computers score : {}".format(self.cs))

        self.games += 1

    def diceGen(self):
        # Generating the playerse dice objects
        self.playerDice = [Die() for i in range(self.numdice)]

        # Generating computers dice object s
        self.comDice = [Die() for i in range(self.numdice)]

        # Generating the dices value
        for i in range(self.numdice):
            # Players dice geneartion
            self.playerDice[i].genDie()

            # Computers dice generation
            self.comDice[i].genDie()


Game()
