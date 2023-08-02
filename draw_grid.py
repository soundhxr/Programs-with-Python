import turtle
draw = turtle.Turtle()
draw.screen.bgcolor("black")
draw.pencolor("white")
draw.pensize(10)
draw.speed(2)

h = int(input("Enter height of the grid: "))
w = int(input("Enter width of the grid: "))
l = 100
n = 0
while True:
    if h > 8*(2**n) or w > 16*(2**n):
        l = 50/(2**n)
        draw.speed(10*(2**n))
        draw.pensize(10-2**n)
        n += 1
    else:
        break

draw.penup()
draw.goto(-w*(l/2), h*(l/2))
draw.pendown()
for i in range(2):
    draw.forward(w * l)
    draw.right(90)
    draw.forward(h * l)
    draw.right(90)

for i in range(w-1):
    draw.forward(l)
    draw.right(90)
    draw.forward(h*l)
    draw.back(h*l)
    draw.left(90)

draw.penup()
draw.goto(-w*(l/2), h*(l/2))
draw.pendown()
draw.right(90)
for i in range(h-1):
    draw.forward(l)
    draw.left(90)
    draw.forward(w*l)
    draw.back(w*l)
    draw.right(90)

turtle.done()
