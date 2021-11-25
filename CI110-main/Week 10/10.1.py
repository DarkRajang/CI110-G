def main():
    # Getting the user input
    ui = eval(input("Enter Score: "))
    # Letter grade for user grade/scores
    gv = []
    b = max(ui)
    for i in ui:
        if i >= b - 10:
            gv.append("A")
        elif i >= b - 20:
            gv.append("B")
        elif i >= b - 30:
            gv.append("C")
        elif i >= b - 40:
            gv.append("D")
        else:
            gv.append("F")

    for i, v in enumerate(gv, 0):  # Assiging the user grade
        print(F"Student {i} score is {ui[i]} and grade is", gv[i])


if __name__ == '__main__':
    main()
