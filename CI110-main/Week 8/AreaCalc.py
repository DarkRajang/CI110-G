from AreaList import *
import time

# User Inputs & Display


def UInDis():
    # Display options
    for i in range(14):
        print("-=", end="")
    print("-")
    print("1) Triangle")
    print("2) Circle")
    print("3) Square")
    print("4) Rectangle")
    print("5) Quit")

    # Users input
    ui = eval(input("Which Shape: "))

    return ui


def ArCalc(ui):
    # Which shape
    a = True
    b = False

    while a == True:
        if b == True:
            ui = eval(input("Which Shape: "))

        if 0 >= ui > 5:
            b = True
            continue

        else:
            if ui == 1:
                a = False
                b = False
                print("The area is:", format(CalcTri(), ".3"))
                print()
            elif ui == 2:
                a = False
                b = False
                print("The area is:", format(CalcCir(), ".3f"))
                print()
            elif ui == 3:
                a = False
                b = False
                print("The area is:", CalcSquare())
                print()
            elif ui == 4:
                a = False
                b = False
                print("The area is:", CalcRec())
                print()
            else:
                return 5


# Getting user inputs for Shapes
# User Input for Triangle area
def CalcTri():
    # Which Shape
    print("\nTriangle Selected:")
    # Users Input
    b, h = eval(input("Base: ")), eval(input("Hight: "))

    return areaTriangle(b, h)
# User Input for Circle


def CalcCir():
    # Which Shape
    print("\nCircle Selected:")
    # Users Input
    r = eval(input("Radius: "))

    return areaCircle(r)

# User Input for Sqaure


def CalcSquare():
    # Which Shape
    print("\nSqaure Selected:")
    # Users Input
    s = eval(input("Side: "))

    return areaSquare(s)

# User Input for Rectangle


def CalcRec():
    # Which Shape
    print("\nRectangle Selected:")
    # Users Input
    l, w = eval(input("Length: ")), eval(input("Width: "))

    return areaRectangle(l, w)

# Looping the calculation


def main():
    print("Shape Calculator")
    x = 0
    while x != 5:
        x = ArCalc(UInDis())
        time.sleep(1)

    print("\nGoodbye")


main()
