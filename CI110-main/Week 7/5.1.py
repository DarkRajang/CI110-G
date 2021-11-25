# Variables
# Postive input
p = 0
# Negative input
n = 0
# Total
t = 0
# Average
avg = 0

# Getting The users input
ui = eval(input("Enter an integer, the input ends if it is 0: "))

# Gathering the users inputs
while ui != 0:
    # Checking if the users input is postive or negative
    if ui % 2 == 0:
        n += 1
    else:
        p += 1

    # Adding the users input to the total
    t += ui

    # Getting The users input
    ui = eval(input("Enter an integer, the input ends if it is 0: "))


# Calculating the average
avg = (t / (p + n))
# Displaying the output
print("\nThe number of postives is {}\nThe Number of negatives {}".format(p, n))
print("Total", t)
print("Average", avg)
