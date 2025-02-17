"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
tina.pendown()
tina.pencolor('red')
tina.forward(70) # Your code here
tina.left() #put the angle in there
tina.pencolor('blue')
tina.forward(70)
tina.left() #put the angle in there
tina.pencolor('purple')
tina.forward(70)

turtle.exitonclick()                    # Close the window when we click on it
