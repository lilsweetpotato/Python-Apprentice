"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes
tina.begin_fill()
tina.circle(75)# Your code here
tina.penup()
tina.color('green')
tina.end_fill()
tina.begin_fill()
tina.goto(-40, 90)
tina.pendown()
tina.circle(20)
tina.color('black')
tina.end_fill()
tina.penup()
tina.goto(40, 90)
tina.begin_fill()
tina.circle(20)
tina.color('black')
tina.end_fill()
tina.goto(10, 50)
tina.begin_fill()
tina.turn(90)
tina.circle(50,180)
tina.color('black')
tina.end_fill()
turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!