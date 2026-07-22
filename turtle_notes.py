import turtle
t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()

t.speed(0)

# I chose a blue background because I wanted my drawing
# to look like a beach scene at night
screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.setup(800, 600)

# I made the sun yellow because it stands out against
# the blue sky
t.penup()
t.goto(200, 100)
t.pendown()

t.pencolor("orange")
t.fillcolor("yellow")
t.pensize(4)

t.begin_fill()
t.circle(60)
t.end_fill()

# I used a few circles together to make my cloud
# instead of making it just one boring shape
t.pencolor("white")
t.fillcolor("white")
t.pensize(2)

t.penup()
t.goto(-250, 150)
t.pendown()

t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-220, 160)
t.pendown()

t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-180, 150)
t.pendown()

t.begin_fill()
t.circle(30)
t.end_fill()

#MY SECOND CLOUD
t.pencolor("white")
t.fillcolor("white")
t.pensize(2)

t.penup()
t.goto(-100, 200)
t.pendown()

t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-70, 210)
t.pendown()

t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-30, 200)
t.pendown()

t.begin_fill()
t.circle(30)
t.end_fill()

# -------------------------
# BEACH / RECTANGLE
# -------------------------

# This rectangle is my beach.
# I used a thicker pen here so the outline is easier to see
t.pensize(5)
t.pencolor("brown")
t.fillcolor("tan")

t.penup()
t.goto(-400, -150)
t.pendown()

t.begin_fill()

# Drawing a rectangle
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(150)
    t.right(90)

t.end_fill()


# I used a different shade of blue for the ocean
t.pensize(3)
t.pencolor("dark blue")
t.fillcolor("royal blue")

t.penup()
t.goto(-400, -150)
t.pendown()

t.begin_fill()

for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)

t.end_fill()


# This is my beach ball.
# The circle also helps me meet the circle requirement
t.pensize(3)
t.pencolor("pink")
t.fillcolor("pink")

t.penup()
t.goto(-250, -275)
t.pendown()

t.begin_fill()
t.circle(40)
t.end_fill()

# PALM TREE TRUNK

t.penup()
t.goto(280, -150)
t.setheading(80)
t.pendown()

t.pencolor("brown")
t.fillcolor("brown")
t.pensize(4)

t.begin_fill()

# Making the trunk using a long rectangle
for i in range(2):
    t.forward(180)
    t.right(90)
    t.forward(35)
    t.right(90)

t.end_fill()


#PALM TREE LEAVES

# Leaf 1
t.penup()
t.goto(300, 30)
t.setheading(20)
t.pendown()

t.pencolor("green")
t.fillcolor("green")

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# Leaf 2
t.penup()
t.goto(300, 30)
t.setheading(90)
t.pendown()

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()


# Leaf 3
t.penup()
t.goto(300, 30)
t.setheading(160)
t.pendown()

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()


# Leaf 4
t.penup()
t.goto(300, 30)
t.setheading(230)
t.pendown()

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()


# Leaf 5
t.penup()
t.goto(300, 30)
t.setheading(300)
t.pendown()

t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# -------------------------
# DOTS AROUND THE SUN
# -------------------------

# I added dots around the sun to make it look brighter.
# I also wanted to make sure I included the dot requirement
# from the marking criteria.

t.pencolor("orange")
t.pensize(2)

# Dot above the sun
t.penup()
t.goto(200, 240)
t.pendown()
t.dot(12)

# Dot below the sun
t.penup()
t.goto(200, 60)
t.pendown()
t.dot(12)

# Dot to the left of the sun
t.penup()
t.goto(110, 150)
t.pendown()
t.dot(12)

# Dot to the right of the sun
t.penup()
t.goto(290, 150)
t.pendown()
t.dot(12)

# Dot in the top-left
t.penup()
t.goto(135, 215)
t.pendown()
t.dot(10)

# Dot in the top-right
t.penup()
t.goto(265, 215)
t.pendown()
t.dot(10)

# Dot in the bottom-left
t.penup()
t.goto(135, 85)
t.pendown()
t.dot(10)

# Dot in the bottom-right
t.penup()
t.goto(265, 85)
t.pendown()
t.dot(10)

# I added a title to make the final picture feel
# more like a finished project
t.penup()
t.goto(-100, 0)
t.pencolor("dark blue")
t.write("My Beach Scene", font=("Arial", 20, "bold"))


turtle.mainloop()
