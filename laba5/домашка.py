import turtle
turtle.shape("turtle")
turtle.color("green")
turtle.speed(5)


for _ in range(4):
    turtle.forward(100)
    turtle.left(90)


turtle.left(135)
turtle.forward(70.7)
turtle.right(90)
turtle.forward(70.7)


turtle.penup()
turtle.goto(40, -100)
turtle.pendown()
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)

turtle.penup()
turtle.goto(-40, -40)
turtle.pendown()
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)


turtle.penup()
turtle.goto(10, -40)
turtle.pendown()
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)

turtle.done()
