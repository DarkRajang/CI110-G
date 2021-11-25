# User input
s, g = eval(input('Enter the subtotal and a grantuity rate: '))
# Rate and total
gr = round(s * (g / 100), 2)
t = round(gr + s, 2)
# Output
print('Total:', t, '\nGrantuity rate:', gr)
