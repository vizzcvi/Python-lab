import turtle


t = turtle.Turtle()
t.shape("turtle")
t.speed(5)

size = 100
angle = 140
color = "green"

t.color(color)

for i in range(3):
    t.forward(size)
    t.left(angle)

turtle.done()

