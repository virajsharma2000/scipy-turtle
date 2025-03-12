import turtle
import random

def draw_bar(t, x, height, width=20):
    """Draws a single bar at position x with the given height and width."""
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def draw_histogram(data):
    """Draws a histogram based on the given data list."""
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Histogram Visualization")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.fillcolor("blue")
    
    bar_width = 30
    spacing = 10
    start_x = -((len(data) * (bar_width + spacing)) // 2)
    
    for i, value in enumerate(data):
        x = start_x + i * (bar_width + spacing)
        draw_bar(t, x, value, bar_width)
    
    t.hideturtle()
    screen.mainloop()

def main():
    random.seed(42)
    data = [random.randint(50, 200) for _ in range(10)]  # Generate random histogram data
    draw_histogram(data)

main()
