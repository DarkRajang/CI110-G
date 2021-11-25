import random


class Die:
    # setting up a defult value for the die
    def __init__(self, v=0, f="|   |\n|   |\n|   |"):
        # Defining the value to self
        self.__value = v
        self.__face = f
        self.__side = [1, 2, 3, 4, 5, 6]

    # Manualy Setting a value to the dice
    def setValue(self, v):
        self.__value = v

    # Manual Setting the face of the die
    def setFace(self, f):
        self.__face = f

    # Return the dice face
    def getValue(self):
        return self.__value

    def getFace(self):
        self.genFace()

        return self.__face

    def genFace(self):
        # Matching the value to a face
        if self.__value == 1:
            self.__face = "|   |\n| * |\n|   |"

        elif self.__value == 2:
            self.__face = "|*  |\n|   |\n|  *|"

        elif self.__value == 3:
            self.__face = "|*  |\n| * |\n|  *|"

        elif self.__value == 4:
            self.__face = "|* *|\n|   |\n|* *|"

        elif self.__value == 5:
            self.__face = "|* *|\n| * |\n|* *|"

        elif self.__value == 6:
            self.__face = "|* *|\n|* *|\n|* *|"

        else:
            self.__face = "|   |\n|   |\n|   |"

    def genDie(self):
        # Getting a value for the die if one has not been set
        if self.__value != self.__side:
            self.__value = random.randint(1, 6)
        # Generating the face for the set value
        self.genFace()
