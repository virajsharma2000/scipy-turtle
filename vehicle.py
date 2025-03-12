import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(3)

# Function to draw the chassis frame
def draw_chassis():
    t.penup()
    t.goto(-150, -50)  # Starting point (Left-bottom)
    t.pendown()
    t.color("black", "gray")
    t.begin_fill()

    # Draw chassis structure
    t.forward(300)  # Bottom frame (300px)
    t.left(90)
    t.forward(50)   # Height 50px (Back)
    t.left(45)
    t.forward(50)   # Rear curve
    t.left(45)
    t.forward(200)  # Top frame (200px)
    t.left(45)
    t.forward(50)   # Front curve
    t.left(45)
    t.forward(50)   # Front vertical
    t.left(90)

    t.end_fill()

    # Label chassis
    t.penup()
    t.goto(-160, -70)
    t.pendown()
    t.write("Car Chassis Frame (300x100)", font=("Arial", 10, "normal"))

# Function to mark wheel axle positions
def draw_axles():
    positions = [(-100, -55), (100, -55)]  # Front & rear axle positions
    for pos in positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.color("black")
        t.circle(5)  # Mark axle as small circle

    # Label axles
    t.penup()
    t.goto(-120, -80)
    t.pendown()
    t.write("Axle Mounting Points", font=("Arial", 8, "normal"))

# Function to mark engine and suspension mounts
def draw_mounting_points():
    mounts = [(-50, -30), (50, -30)]  # Approximate mounting locations
    for mount in mounts:
        t.penup()
        t.goto(mount)
        t.pendown()
        t.color("red")
        t.begin_fill()
        t.circle(3)  # Engine and suspension mounts
        t.end_fill()

    # Label mounting points
    t.penup()
    t.goto(-70, -20)
    t.pendown()
    t.write("Engine & Suspension Mounts", font=("Arial", 8, "normal"))

# Draw all parts of chassis
def assemble_chassis():
    draw_chassis()
    draw_axles()
    draw_mounting_points()

assemble_chassis()
turtle.done()
