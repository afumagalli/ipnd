import turtle

def draw_square(turtle):
	for i in range(4):
		turtle.forward(100)
		turtle.right(90)

def draw_circle(turtle):
	turtle.circle(100)

def draw_triangle(turtle):
	for i in range(3):
		turtle.forward(100)
		turtle.left(120)

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")

	george = turtle.Turtle()
	george.shape("circle")
	george.color("green")

	draw_square(brad)
	draw_circle(angie)
	draw_triangle(george)

	window.exitonclick()

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")

	for i in range(36):
		draw_square(brad)
		brad.right(10)

import turtle
def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(100,5)
window.exitonclick()

#draw_art()