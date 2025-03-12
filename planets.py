import turtle
import math

# planet movement

def main():
   
# Setup screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Planetary Orbit Simulation")

    # Create Sun (static)
    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(2)  # Scale sun size

    # Create Planet
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color("blue")
    planet.shapesize(0.7)
    planet.penup()
    planet.goto(100, 0)  # Start position
    planet.pendown()
    planet.speed(0)

    # Orbit parameters
    a = 150  # Semi-major axis
    b = 100  # Semi-minor axis
    theta = 0

    # Planet motion
    while True:
        x = a * math.cos(math.radians(theta))
        y = b * math.sin(math.radians(theta))
        planet.goto(x, y)
        theta += 1  # Increment angle
        if theta >= 360:
            theta = 0  # Reset for continuous motion




if __name__ == "__main__":
    main()
