import turtle
soundher = turtle.Turtle()
sides = int(input("How many sided polygon do you want to print? "))
for i in range(sides):
    soundher.right(360/sides)
    soundher.forward(100)
