p1w, p1p = eval(input("Enter the weight and price for package 1: "))
p2w, p2p = eval(input("Enter the weight and price for package 2: "))

p1 = p1w / p1p
p2 = p2w / p2p

if p1 < p2:
    print("Package 1 has a better price.")
else:
    print("Package 2 has a better price.")
