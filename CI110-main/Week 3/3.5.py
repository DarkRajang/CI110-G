import math

s, l = eval(input('Input the number of side for the Polygon: ')
            ), float(input('Enter the length of the sides: '))

a = (l * (s**2)) / (4 * math.tan(math.pi / l)) * 6.5

print('The area of the polygon is {}'.format(a))
