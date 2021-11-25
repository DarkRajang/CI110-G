# Users Input
def UIn():
    # Getting the user new pin and username
    # User name
    un = input(("Please enter your new username: "))
    # User Pin
    up = eval(input("Please enter your new pin: "))
    # User pin again
    upa = eval(input("Please enter your new pin again: "))

    # Checking if User pin matchs user pin again
    if upa != up:
        while upa != up:
            upa = eval(input("Pin does not match try again: "))

    return un, upa


def TestLogCred(un, up):
    print("\nLet's test your user login credentials.\n" +
          "You will get 3 tries to enter your pin.")

    # Testing Username
    return TestUCred(un), TestPinCred(up)


# Testing Username Credentials
def TestUCred(un):
    # Get username
    cun = input("Please enter your username: ")

    # Chechking if the username matched the stored user name
    if un == cun:
        x = True
        return x
    else:
        while un != cun:
            cun = input("Invalid username try again: ")

# Testing Pin Credentials


def TestPinCred(up):
    y = True
    t = 1
    # Get Pin
    # Chechking if the Pin matched the stored Pin
    cup = eval(input("Please enter your pin: "))
    if cup == up:
        return y
    else:
        # If the first input does not match
        for i in range(2):
            t += 1
            cup = eval(input("Try {} Invailid pin try again: ".format(t)))
            if t == 3:
                y = False
                return y

# main Program


def main():
    print("Welcome to my MVCC")
    # Username, User Pin
    un, up = UIn()
    # Correct Username, Correct Pin
    cn, cp = TestLogCred(un, up)

    if cn is True and cp is True:
        print("\nLog in credentails accpeted. Welcome to my MVCC")
    else:
        print("\nTo many log in attempted. Account locked out.")


main()
# un, up = UIn()
# print(TestLogCred(un, up))

# up = eval(input(": "))
# print(TestPinCred(up))
