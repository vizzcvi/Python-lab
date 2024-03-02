import turtle
star = turtle.Turtle()
star.speed(5)
num_points = 5
angle = 180 - (180 / num_points)

for _ in range(num_points):
    star.forward(100)
    star.right(angle)

turtle.done()