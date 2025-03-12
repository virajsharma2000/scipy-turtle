import turtle
import math

## hexagonal and cubic crystal structures using turtle. The hexagonal lattice represents molecular arrangements in semiconductors, while the cubic lattice represents metals.


def draw_hexagon(t, x, y, size):
    """Draws a hexagon centered at (x, y) with a given size."""
    t.penup()
    t.goto(x + size * math.cos(math.radians(30)), y + size * math.sin(math.radians(30)))
    t.pendown()
    for _ in range(6):
        t.forward(size)
        t.right(60)

def draw_hexagonal_lattice(t, rows, cols, size):
    """Draws a hexagonal crystal lattice with specified rows and columns."""
    t.color("cyan")
    
    for row in range(rows):
        for col in range(cols):
            x = col * 1.5 * size
            y = row * math.sqrt(3) * size
            if col % 2 == 1:
                y += math.sqrt(3) / 2 * size  # Offset odd columns
            draw_hexagon(t, x - 200, y, size)  # Shift left for better spacing

def draw_cubic_lattice(t, rows, cols, size):
    """Draws a cubic crystal lattice as a simple grid."""
    t.color("yellow")
    
    for row in range(rows):
        for col in range(cols):
            x = col * size * 2
            y = row * size * 2
            t.penup()
            t.goto(x + 100, y)  # Shift right for better spacing
            t.pendown()
            for _ in range(4):
                t.forward(size)
                t.right(90)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Crystal Structures")

    t = turtle.Turtle()
    t.speed(0)

    # Draw structures
    draw_hexagonal_lattice(t, 5, 5, 30)
    draw_cubic_lattice(t, 5, 5, 30)

    t.hideturtle()
    screen.mainloop()

main()
