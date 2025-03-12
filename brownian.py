import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

for _ in range(1000):  # Simulate 1000 random steps
    t.forward(5)
    t.setheading(random.randint(0, 360))

turtle.done()