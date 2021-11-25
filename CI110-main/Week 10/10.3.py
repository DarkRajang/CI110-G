def ui():  # Getting the user input
    ui = eval(input("Enter integers between 1 and 100: "))
    return ui


# Sort and check
def snc(ui):
    ui.sort(reverse=True)  # Sorting the list in decending order
    x = set(ui)  # Getting rid of any duplicates
    for x in x:  # Looping through the set and taking the count for the number
        oc = ui.count(x)
        print(F"{x} occurs {oc} times")


def main():
    snc(list(ui()))


if __name__ == '__main__':
    main()
