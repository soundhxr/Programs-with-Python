import turtle
shape = int(input("Which shape do you want to draw?\n1 - Star\n2 - Heart\n3 - Sun\n4 - Flower\nEnter the number corresponding to the shape you want to draw: "))
draw = turtle.Turtle()
draw.screen.bgcolor("black")
draw.pencolor("white")
draw.pensize(10)
draw.speed(1)

def goto(x, y):
    draw.penup()
    draw.goto(x,y)
    draw.pendown()
def fwd(x):
    draw.penup()
    draw.forward(x)
    draw.pendown()

if shape == 1:
    goto(-250, 100)
    for i in range(5):
        draw.forward(500)
        draw.right(144)
    turtle.done()

if shape == 2:
    draw.pencolor("red")
    goto(0, - 300)
    draw.left(45)
    draw.forward(400)
    draw.circle(200, 180)
    draw.right(90)
    draw.circle(200, 180)
    draw.forward(400)
    turtle.done()

if shape == 3:
    draw.pencolor("yellow")
    goto(0, -200)
    draw.circle(200, 360)
    for i in range(10):
        draw.circle(200, 36)
        draw.right(90)
        fwd(30)
        draw.forward(120)
        draw.back(120)
        draw.penup()
        draw.back(30)
        draw.pendown()
        draw.left(90)
    turtle.done()

if shape == 4:
    draw.pencolor("pink")
    goto(-150, -150)
    draw.right(90)
    for i in range(4):
        draw.circle(150, 180)
        draw.right(90)
    goto(0,-100)
    draw.left(90)
    draw.circle(100, 360)
    turtle.done()
