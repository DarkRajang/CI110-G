import turtle

# Getting the radius from the user
r = eval(input('Give me a radius: '))

turtle.showturtle()
turtle.penup()
turtle.goto(r, r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(-r, -r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(-r, r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(r, -r)
turtle.pendown()
turtle.circle(r)
turtle.bye()
