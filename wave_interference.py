import turtle
import math

t = turtle.Turtle()
t.speed(0)

for x in range(-360, 360):
    y = 50 * math.sin(math.radians(x))
    t.goto(x, y)

turtle.done()