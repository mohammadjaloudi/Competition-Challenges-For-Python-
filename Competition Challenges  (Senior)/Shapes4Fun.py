import turtle

sc = turtle.Screen()
sc.setup(500, 500)
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

shapes = ["square", "triangle", "rectangle", "circle"]
sizes = ["small", "medium", "large"]
colors = ["red", "green", "blue", "orange", "yellow"]

def square(size, color):
    side = 100
    if size == "small":
        side = 50
    elif size == "medium":
        side = 70
    
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(side)
        pen.left(90)
    pen.end_fill()

    
def triangle(size, color):
    side = 100
    if size == "small":
        side = 50
    elif size == "medium":
        side = 70
    
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(side)
        pen.left(120)
    pen.end_fill()

    
def rectangle(size, color):
    fside = 100
    sside = 80
    if size == "small":
        fside = 50
        sside = 40
    elif size == "medium":
        fside = 70
        sside = 55
    
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(fside)
        pen.left(90)
        pen.forward(sside)
        pen.left(90)
    pen.end_fill()

    
def circle(size, color):
    side = 100
    if size == "small":
        side = 50
    elif size == "medium":
        side = 70
    
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(side)
    pen.end_fill()

shape = "0"
color = "0"
size = "0"
while True:
    if shape not in shapes:
        shape = input("Enter the shape square, triangle, rectangle, circle or -1 to stop: ")
        if shape == "-1":
            break
        shape = shape.lower()
        if shape not in shapes:
            print("Invalid shape")
            continue
    if color not in colors:
        color = input("Enter the color: red, green, blue, orange, yellow or -1 to stop: ")
        if color == "-1":
            break
        color = color.lower()
        if color not in colors:
            print("Invalid color")
            continue
    if size not in sizes:
        size = input("Enter the size small, medium, large or -1 to stop: ")
        if size == "-1":
            break
        size = size.lower()
        if size not in sizes:
            print("Invalid size")
            continue
    
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    sc.clear()
    
    if shape == "square":
        square(size, color)
    elif shape == "triangle":
        triangle(size, color)
    elif shape == "rectangle":
        rectangle(size, color)
    else:
        circle(size, color)
    
    shape = size = color = "0"
    
    con = input("Do you want to continue? Enter YES if you want to continue, otherwise enter anything: ")
    if con.upper() != "YES":
        break

turtle.exitonclick()
