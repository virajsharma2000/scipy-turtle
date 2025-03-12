import turtle

# Create the circle 
t = turtle.Screen()
t.bgcolor('black')

circle = turtle.Turtle()

circle.shape("circle")
circle.color("blue")

while True:
  circle.circle(100)