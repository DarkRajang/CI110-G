# User Inputs
def UIn():

    # User input
    u1 = eval(input('Give me a number: '))
    u2 = eval(input('Give me a number: '))
    u3 = eval(input('Give me a number: '))

    return u1, u2, u3


def findMAX(u1, u2, u3):

    # Finding which nubmer is largest
    if u1 > u2 and u1 > u3:
        return u1
    elif u2 > u1 and u2 > u3:
        return u2
    elif u3 > u1 and u3 > u2:
        return u3
    else:
        return u1


def main():
    # Calling and distrubting User input
    u1, u2, u3 = UIn()
    return print(findMAX(u1, u2, u3))


main()
