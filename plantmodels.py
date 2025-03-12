import turtle

def tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        tree(branch_length - 15, t)
        t.left(40)
        tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()
tree(100, t)
turtle.done()