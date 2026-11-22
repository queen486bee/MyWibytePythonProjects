# Im sorry this was very late. It took me a long time to finish the code since I didn't have much time after school and Badminton.
# This midterm project is like the Snake Game that we did in Scratch but it is with brains instead, so I can make projects and practice more related to Neuro.
import turtle
import random
import time

# Set up the game screen
ts = turtle.Screen()
ts.setup(width=600, height=600)
ts.bgcolor("#f5e6ed")
ts.title("BRAIN QUEST: Neuroscience Snake")

# I made my own brain shape instead of using regular squares.
# It's not that good, but hopefully it works.
brain_points = (
    (-12, -4), (-12, 1), (-10, 6), (-7, 9),
    (-3, 8), (0, 11), (4, 10), (8, 8),
    (11, 4), (12, 0), (10, -4), (7, -8),
    (3, -9), (0, -7), (-4, -9), (-8, -8),
    (-11, -6)
)

# I saved my custom brain shape.
ts.register_shape("brain", brain_points)


# This Creates the player (the snake's head).
t = turtle.Turtle()
t.shape("square")
t.color("#65365e")
t.penup()
t.speed(0)


# I will keep track of the brains collected and the snake's tail with the following code.
brains_collected = 0
segments = []


# This creates the food turtle, aka brain for this game.
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("brain")
food.color("#a64d79", "#f4a6c8")


# This is a function to make a brain appear at a random location.
def make_brain():

    # I don't want the brain appearing on top of my player or tail.
    while True:
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)

        if t.distance(x, y) > 40:

            if all(segment.distance(x, y) > 30 for segment in segments):
                break

    food.goto(x, y)


# Make the first brain appear.
make_brain()


# This will help to display the total number of brains collected.
pen = turtle.Turtle()
pen.penup()
pen.goto(0, 255)
pen.color("#65365e")
pen.ht()


# This will help to display the number of lives remaining.
life_pen = turtle.Turtle()
life_pen.penup()
life_pen.goto(0, 225)
life_pen.color("#d6336c")
life_pen.ht()


# This will help to display the final game message.
report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("#65365e")
report.ht()


# Lives, because I want to keep track of it, and so it is not a never-ending game.
lives = 2
game_over = False


# I created a function for when the player loses a life. This will make my polayer go back to the orginal place.
# The score will not reset because I wanna give a chance to the people playing this game. 
#BEWARE there is only 2 lives.
def lose_life():

    global lives, game_over

    lives = lives - 1

    # Send the player back to the center.
    t.goto(0, 0)
    t.setheading(0)

    # Reset the brain tail positions.
    for segment in segments:
        segment.goto(0, 0)

    # The game ends when both lives are gone.
    if lives == 0:
        game_over = True


# These functions control which direction my player moves.
def right():
    if t.heading() != 180.0:
        t.setheading(0.0)


def left():
    if t.heading() != 0.0:
        t.setheading(180.0)


def up():
    if t.heading() != 270.0:
        t.setheading(90.0)


def down():
    if t.heading() != 90.0:
        t.setheading(270.0)


# This connects the arrow keys to the movement functions.
ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()


# Main game loop.
while game_over == False:


    # This will update the total number of brains collected.
    pen.clear()
    pen.write("Brains Collected: " + str(brains_collected),
              align="center", font=("Courier", 18, "bold"))

    # This will update the lives display.
    life_pen.clear()
    life_pen.write("Lives: " + str(lives),
                   align="center", font=("Arial", 16, "bold"))


    # Check if the player collects a brain.
    if t.distance(food) < 20:

        brains_collected = brains_collected + 1

        # This creates a new brain-shaped tail segment.
        segment = turtle.Turtle()
        segment.penup()
        segment.speed(0)
        segment.shape("brain")
        segment.color("#a64d79", "#f4a6c8")
        segment.goto(t.xcor(), t.ycor())

        segments.append(segment)

        # Moves the collectible to a completely new location.
        # This allows the game to continue.
        make_brain()


    # This Moves the tail segments in reverse order.
    for index in range(len(segments) - 1, 0, -1):

        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()

        segments[index].goto(x, y)


    # This moves the first tail segment to the player's previous position.
    if len(segments) > 0:

        x = t.xcor()
        y = t.ycor()

        segments[0].showturtle()
        segments[0].goto(x, y)


    # Check where the player is going BEFORE moving.
    next_x = t.xcor()
    next_y = t.ycor()

    if t.heading() == 0:
        next_x = next_x + 20

    elif t.heading() == 180:
        next_x = next_x - 20

    elif t.heading() == 90:
        next_y = next_y + 20

    elif t.heading() == 270:
        next_y = next_y - 20


    # Check if the player hits a screen border.
    if (next_x > 270 or next_x < -270 or
        next_y > 270 or next_y < -270):

        # Lose a life if the player hits a border.
        lose_life()

    else:

        # Move the player if it stays inside the screen.
        t.forward(20)

        # Check if the player touches any part of its own tail.
        for segment in segments:

            if t.distance(segment) < 18:

                # Lose a life if the player bites its own tail.
                lose_life()
                break


    time.sleep(0.1)


# This will hide the player and tail after the game ends.
t.ht()
food.ht()

for segment in segments:
    segment.ht()


# Display the final score and game-over message.
#It will display a game over sign with the amount of brains collected.
pen.clear()
life_pen.clear()

report.write("GAME OVER!",
             align="center", font=("Courier", 22, "bold"))

report.goto(0, -35)
report.write("Brains Collected: " + str(brains_collected),
             align="center", font=("Courier", 16, "normal"))




time.sleep(2)

# Keep the game window open.
ts.mainloop()


# I made a game that has brains in it because of my interest in
# neuroanatomy and neuroscience.
