# User input for feet
f = eval(input('Give me a measure in feet: '))
# Feet to meters
m = f / 3.27868852
x = '{}\" in Meters is {}'
print(x.format(f, m))
