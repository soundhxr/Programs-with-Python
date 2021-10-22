import turtle
draw = turtle.Turtle()
draw.speed(10)
draw.pensize(10)
q=0
draw.penup()
draw.goto(-400, -400)
draw.pendown()
def sqr():
    for i in range(4):
        draw.forward(100)
        draw.left(90)
    draw.forward(100)
lst = list(range(8))
for w in range(8):
    if w%2 == 1:
        lst = list(range(1, 9))
    else:
        lst = list(range(8))
    for d in lst:
        if d % 2 == 1:
            sqr()
        if d % 2 == 0:
            draw.color("black")
            draw.begin_fill()
            sqr()
            draw.end_fill()
    q += 1
    draw.penup()
    draw.goto(-400, -400 + (q * 100))
    draw.pendown()

turtle.done()
