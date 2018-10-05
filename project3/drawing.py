#This program implements a loop and draws a turtle art using the turtle module

#Run python shell by typing "python3" then type "import drawing" then "drawing.drawpic()"


import turtle
import math
import time

def leaf_right(t, angl, forw):
	t.left(angl)
	t.forward(forw)

def leaf_left(t, angl, forw):
	t.right(angl)
	t.forward(forw)


def drawpic():
	change = 0
	
	#a super cute turtle draws my picture and this mode sets the whole drawing color to pink
	turtle.shape("turtle")
	turtle.colormode(255)
	turtle.color(215, 100, 170)

	turtle.speed(0)
	
	#draws the flower
	for angle in range(0, 360, 15):
		turtle.seth(angle)
		turtle.circle(50)
#	time.sleep(0.1)


	turtle.penup()
	turtle.position()
	turtle.pendown()

	#draws the stem
	turtle.pencolor("green")
	turtle.pensize(5)
	turtle.right(75)
	turtle.forward(200)
	turtle.fillcolor("green")

	#draws the right leaf
	turtle.pensize(2)
	turtle.left(75)
	turtle.begin_fill()
	for ang in range(1, 20):
		leaf_right(turtle, ang, 10)
	for ang in range(20, 15, -1):
		leaf_right(turtle, ang, 24)
	turtle.end_fill()


	#draws the left leaf
	turtle.penup()
	yaxis = turtle.ycor()
	turtle.setposition(0, yaxis)
	turtle.pendown()
	turtle.right(80)
	turtle.begin_fill()
	for ang in range(1, 20):
		leaf_left(turtle, ang, 10)
	for ang in range(20, 15, -1):
		leaf_left(turtle, ang, 25)
	turtle.end_fill()


	turtle.exitonclick()
