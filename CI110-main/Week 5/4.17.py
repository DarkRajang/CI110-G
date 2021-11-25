import random

ct = random.randint(0, 2)

ut = eval(input("scissor (0), rock(1), paper (2): "))

if ct == 0:
    if ut == 1:
        print("The computer is scissor. You are rock. You won.")
    elif ut == 2:
        print("The computer is scissor. You are paper. You lose.")
    else:
        print("The computer is scissor. You are scissors. It is a draw")
elif ct == 1:
    if ut == 2:
        print("The computer is rock. You are paper. You won.")
    elif ut == 0:
        print("The computer is rock. You are scissors. You lose.")
    else:
        print("The Ccomputer is rock. You are rock. It is a draw ")
elif ct == 2:
    if ut == 0:
        print("The computer is paper. You are scissors. You won")
    elif ut == 1:
        print("The computer is paper. You are rock. You lose.")
    else:
        print("The computer is paper. You are paper. It is a draw")
