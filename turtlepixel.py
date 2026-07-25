import turtle
import random

t = turtle.Turtle()
turtle_screen = t.getscreen()

t.speed(0)
t.hideturtle()

# This makes the picture appear faster.
turtle_screen.tracer(0)


# This function draws one filled-in pixel.
# I can reuse this function instead of writing the
# same drawing instructions every time.
def draw_pixel(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for i in range(4):
        t.forward(size)
        t.left(90)

    t.end_fill()


# I used a for loop so I don't have to draw
# every single square separately.

y = 300

for row in range(25):
    x = -400

    # This changes the color depending on
    # which row we are drawing.
    if row < 8:
        color = "lightblue"
    elif row < 16:
        color = "gold"
    else:
        color = "orange"

    # Draw 40 pixels across each row.
    for column in range(40):
        draw_pixel(x, y, 20, color)
        x = x + 20

    # Move down 20 pixels for the next row.
    y = y - 20


# I placed the ocean directly below the sunset sky.
# I used multiple rows of pixels to make the ocean.

y = -200

for row in range(7):
    x = -400

    # I used if/elif/else to give the ocean
    # different shades of blue.
    # The only shades of blue the work is light blue and regular blue. But I don't really want to use light blue
    # This might be an unnessacary if, else code
    if row < 5:
        color = "blue"
    else:
        color = "dark blue"

    # This draws 40 pixels across each row.
    for column in range(40):
        draw_pixel(x, y, 20, color)
        x = x + 20

    # Move down 20 pixels for the next row.
    y = y - 20


# ---------------------------------
# SUN
# ---------------------------------

# I made the sun using yellow pixels.
# I placed it in the middle of the sunset sky.

draw_pixel(-40, 40, 20, "yellow")
draw_pixel(-20, 40, 20, "yellow")
draw_pixel(0, 40, 20, "yellow")
draw_pixel(20, 40, 20, "yellow")
draw_pixel(40, 40, 20, "yellow")

draw_pixel(-40, 20, 20, "yellow")
draw_pixel(-20, 20, 20, "yellow")
draw_pixel(0, 20, 20, "yellow")
draw_pixel(20, 20, 20, "yellow")
draw_pixel(40, 20, 20, "yellow")

draw_pixel(-40, 0, 20, "yellow")
draw_pixel(-20, 0, 20, "yellow")
draw_pixel(0, 0, 20, "yellow")
draw_pixel(20, 0, 20, "yellow")
draw_pixel(40, 0, 20, "yellow")

# Cloud 1
draw_pixel(-260, 140, 20, "white")
draw_pixel(-240, 140, 20, "white")
draw_pixel(-220, 140, 20, "white")
draw_pixel(-200, 140, 20, "white")

draw_pixel(-240, 160, 20, "white")
draw_pixel(-220, 160, 20, "white")

# Cloud 2
draw_pixel(120, 100, 20, "white")
draw_pixel(140, 100, 20, "white")
draw_pixel(160, 100, 20, "white")
draw_pixel(180, 100, 20, "white")

draw_pixel(140, 120, 20, "white")
draw_pixel(160, 120, 20, "white")

# Cloud 3
draw_pixel(250, 190, 20, "white")
draw_pixel(270, 190, 20, "white")
draw_pixel(290, 190, 20, "white")
draw_pixel(310, 190, 20, "white")

draw_pixel(270, 210, 20, "white")
draw_pixel(290, 210, 20, "white")


# I used small groups of pixels to make waves.
# The waves are repeated across the ocean.

y = -230 #Row where the waves would be
x = -400 #Starts from the left 

for i in range(40): #Go across the whole screen
    x = -380 + (i * 80)

    # Each wave has 3 light-colored pixels.
    draw_pixel(x, y, 20, "white")
    draw_pixel(x + 20, y, 20, "lightblue")
    draw_pixel(x + 40, y, 20, "white")

    # This second row makes the wave pattern
    # look more interesting and less like one straight line.
    draw_pixel(x + 20, y + 20, 20, "white")

x = x + 40


# Like my previous project (Activity 7), I made a sunset and ocean here because I wanted to elaborate on my prevoius piece and make it better with pixels.
turtle.mainloop()
