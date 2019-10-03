# Author: Jessica Strait
# This project implements turtle graphics to draw and color a polygon- with a turtle shaped cursor.

# Let's begin by importing the two modules we will need: turtle graphics and random for the randint function.
import turtle
import random

# Next, we will specify some drawing variables: a screen for drawing, a turtle drawing icon, and the color list.
screen = turtle.Screen()
polygon = turtle.Turtle('turtle')
colorsList = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan', 'pink', 'magenta',
              'goldenrod']

# Here is our function to actually draw the polygon. We must include aspects relating to size, angle, and color within the required "for" loop to create any polygon specified by the user.


def makePolygon(sides, length, borderColor, width, fillColor):
    polygon.pen(fillcolor=fillColor, pencolor=borderColor, pensize=width)
    polygon.begin_fill()
    for x in range(sides):
        polygon.down()
        polygon.forward(length)
        polygon.left(360/sides)
        polygon.up()
    polygon.end_fill()

# We will use this Boolean expression within our while loop to allow for many polygons to be drawn.
keepGoing = True

# Our while loop will have an if loop to verify that the number of sides is at least three. We will specify the parameters that will be used in our function. Then, we call the function!
while keepGoing:
    sides = int(input("Enter a number of sides for your polygon, or enter a number less than 3 to end."))
    if sides < 3:
        keepGoing = False
        print("Thank you for using the polygon generator!")
    else:
        polygon.clear()
        length = (600 / sides)
        width = (sides % 20) + 1
        borderColor = colorsList[random.randint(0, 12)]
        fillColor = colorsList[random.randint(0, 12)]
        makePolygon(sides, length, borderColor, width, fillColor)
