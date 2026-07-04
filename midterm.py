# OPERATION: SECRET VAULT
# By: Arshiya
# -----------------------------------------

import random

score = 0

print("=" * 45)
print("      OPERATION: SECRET VAULT")
print("=" * 45)
print()

#Prints the = sign, 45 times
#Introduction of the game

print("Welcome, Agent!")
print("The world's most valuable vault has been locked.")
print("Your mission is to break in before security catches you.")
print("Complete all four levels to win.")
print()

#We need to answer questions and solve riddles to unlock the secret vault and finish the mission. 
#Enter your agent name

agent = input("Enter your agent name: ").strip().title()

print()
print("Welcome,", agent + "!")
print("Good luck...")
print()

input("Press ENTER to begin your mission...")
print()

# -------------------------------------------------
# LEVEL 1 - PASSWORD
# -------------------------------------------------

print("=" * 45)
print("LEVEL 1 - SECURITY PASSWORD")
print("=" * 45)

password = "shadow"
attempts = 3

#Password is shadow. There are 3 attempts to guess it. This is the first challenge. Good luck to guess the password!!
#There will be some hints if you get the first attempt wrong. Just pick a random word for the first try.

while attempts > 0:
    answer = input("Enter the password: ").strip().lower()

    if answer == password:
        print("Access Granted!")
        score += 10
        break

    else:
        attempts -= 1

        if attempts == 2:
            print("Incorrect!")
            print("Hint: It appears when light is blocked.")

        elif attempts == 1:
            print("Incorrect!")
            print("Hint: It starts with the letter S.")

        else:
            print()
            print("MISSION FAILED")
            print("Security has been alerted!")
            print("The password was:", password)
            exit()

print()

# -------------------------------------------------
# LEVEL 2 - MATH CHALLENGE
# -------------------------------------------------

print("=" * 45)
print("LEVEL 2 - SECURITY SCANNER")
print("=" * 45)

# For this second challenge, answer different math questions. They are relatively simple. It is kind of like the missing operators but instead of finding the operators we are just adding the numbers.
for i in range(3):

    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    answer = int(input(str(num1) + " + " + str(num2) + " = "))

    if answer == num1 + num2:
        print("Correct!")
        score += 10
    else:
        print("Incorrect.")
        print("Answer:", num1 + num2)
        print("Security has been alerted")
        exit()

#you can only move on if you get all the 3 questions right. Good luck.
    print()

# -------------------------------------------------
# LEVEL 3 - GUESS THE CODE
# -------------------------------------------------

print("=" * 45)
print("LEVEL 3 - CRACK THE VAULT")
print("=" * 45)

#Moved onto Level 3, which is guessing the code. 
secret = random.randint(1,5)
attempts = 2

#This gives you 2 attempts to guess the code. If you get one wrong, you get a tiny hint for the other chance. Also, security will be alerted if you get it wrong.
while attempts > 0:
    guess = int(input("Guess the vault code (1-5): "))

    if guess == secret:
        print("Correct!")
        print("The vault door is opening...")
        score += 15
        break
    else:
        attempts -= 1

        if attempts == 1:
            print("Incorrect!")
            print("Hint: The code is", "higher." if guess < secret else "lower.")
            print("You have 1 attempt left.\n")

        else:
            print("ALERT!")
            print("Security has been notified!")
            print("The correct code was", secret)
            exit()
# break immediately stops the loop and moves to the next part of the program
print()

# -------------------------------------------------
# LEVEL 4 - LASER MAZE
# -------------------------------------------------

print("=" * 45)
print("LEVEL 4 - LASER MAZE")
print("=" * 45)

#Now we are on level 4 which makes you choose a random path. You will still escape but you might activate the laser. 

print("Choose your path")
print("1. Left")
print("2. Right")
print("3. Straight")

safe = random.randint(1,3)

choice = int(input("Choose a path: "))

if choice == safe:
    print("You avoided every laser!")
    score += 15

else:
    print("Laser Activated!")
    print("You escaped... but barely!")

print()

# -------------------------------------------------
# FINAL SCORE
# -------------------------------------------------

#I used a variable called score that starts at 0. Whenever the player completes a challenge successfully, I add points using score +=. The points from each level are added together to calculate the final score out of 70.
#Password Challenge: +10 points
#Math Challenge: +10 points for each correct question (3 questions = 30 points)
#Vault Code Challenge: +15 points
#Laser Maze: +15 points
#If the exit is reached, since ppl failed the tasks: No more points can be earned, The remaining levels are skipped, and The final score is not displayed.

print("=" * 45)
print("MISSION COMPLETE")
print("=" * 45)

print(agent + ", your final score is", score, "out of 70.")
print()

if score == 70:
    print("★★★★★")
    print("Perfect Mission!")
    print("You are the greatest secret agent!")

elif score >= 50:
    print("★★★★☆")
    print("Excellent work!")
    print("The vault has been secured.")

elif score >= 30:
    print("★★★☆☆")
    print("Mission Complete.")
    print("You made a few mistakes but succeeded.")

else:
    print("★★☆☆☆")
    print("Mission Failed.")
    print("Better luck next time!")

print()
print("Thank you for playing Operation: Secret Vault!")
