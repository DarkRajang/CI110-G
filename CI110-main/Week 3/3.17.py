import turtle

#User input
p1 = x1, y1 = eval(input("P1: "))
p2 = x2, y2 = eval(input("P2: "))
p3 = x3, y3 = eval(input("P3: "))

#Sides
s1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
s2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
s3 = ((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)) ** 0.5

s = (s1 + s2 + s3) / 2
a = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
atxt = 'The area of the triangle is: {}'.format(a)

turtle.penup()
turtle.goto(p1)
turtle.write(p1)
turtle.pendown()
turtle.goto(p2)
turtle.write(p2)
turtle.goto(p3)
turtle.write(p3)
turtle.goto(p1)
turtle.penup()
turtle.goto(x3 - 50, y3 - 100)
turtle.write(atxt, font=("Arial", 8, "normal"))

turtle.done()