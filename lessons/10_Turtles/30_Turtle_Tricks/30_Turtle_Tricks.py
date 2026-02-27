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
def eye(direction):
  
    tina.right(180*direction)
    tina.forward(35)
    tina.right(90*direction)
    tina.forward(25)
    tina.right(90*direction)
    tina.forward(18)
    tina.right(90*direction)
    tina.forward(25)
    tina.begin_fill()
    tina.left(180*direction)
    tina.forward(25)
    tina.right(90*direction)
    tina.forward(18)
    tina.right(90*direction)
    tina.forward(25)
    tina.color('black')
    tina.end_fill()

def square(side_length):
    for i in range(4):
        tina.forward(side_length)
        tina.left(90)
    

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes
square(150)

tina.goto(0, 150)
tina.begin_fill()
tina.right(90)
tina.forward(40)
tina.left(90)
tina.forward(30)
tina.left(90)
tina.forward(20)
tina.right(90)
tina.forward(90)

tina.right(90)
tina.forward(20)
tina.left(90)
tina.forward(30)
tina.goto(150, 150)
tina.color('brown')
tina.end_fill()

tina.goto(150, 80)


tina.right(180)
tina.forward(35)
tina.right(90)
tina.forward(25)
tina.right(90)
tina.forward(18)
tina.right(90)
tina.forward(25)
tina.begin_fill()
tina.left(180)
tina.forward(25)
tina.right(90)
tina.forward(18)
tina.right(90)
tina.forward(25)
tina.color('black')
tina.end_fill()
tina.penup()

tina.goto(0, 80)
tina.pendown()
tina.right(90)
eye(-1)

tina.penup()
tina.forward(80)
tina.left(90)
tina.forward(50)
tina.left(90)


tina.pendown()
tina.begin_fill()
tina.forward(60)
tina.right(90)
tina.forward(50)
tina.right(90)
tina.forward(60)
tina.color('red')
tina.end_fill()


tina.begin_fill()
tina.left(180)
tina.penup()
tina.forward(60)
tina.left(90)
tina.forward(10)
tina.left(90)
tina.forward(30)
tina.right(90)
tina.forward(40)
tina.color('white')
tina.end_fill()
tina.right(90)
tina.forward(30)



turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!