"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 150  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(60):
    t.pencolor(getRandomColor())

    t.fillcolor('yellow') 
   
    t.begin_fill()

    t.forward(64) 

    t.left(10) 

    t.forward(flameSize) 

    t.right(180) 

    t.forward(flameSize) 

    t.right(68) 

    t.forward(baseSize) 

    t.end_fill()
t.penup()
t.goto(200,200)
t.pencolor('black')
t.write('bill cipher :)')

t.hideturtle() 

turtle.exitonclick() 
