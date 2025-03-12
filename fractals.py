import turtle

def koch_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_snowflake(t, length, depth-1)
        t.left(60)
        koch_snowflake(t, length, depth-1)
        t.right(120)
        koch_snowflake(t, length, depth-1)
        t.left(60)
        koch_snowflake(t, length, depth-1)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 100)
t.pendown()

for _ in range(3):
    koch_snowflake(t, 300, 4)
    t.right(120)

turtle.done()
