
#SECRET AGENT: CODE CRACKER
# My mission is to decode the secret messages!



# 1. Swap even and odd letters

def even_odd_swap(x):
    # I add a space if the length is odd so every
    # character can be paired with another one.
    if len(x) % 2 != 0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ''

    # I switch the order of each pair of characters.
    for i in range(len(even_letters)):
        s = s + odd_letters[i]
        s = s + even_letters[i]

    return s


# 2. Swap the first and second halves

def swap_middle(x):
    # I add a space if needed to make equal halves.
    if len(x) % 2 != 0:
        x = x + ' '

    first_half = x[0:int(len(x) / 2):1]
    second_half = x[int(len(x) / 2)::1]

    # I put the second half before the first half.
    s = second_half + first_half

    return s


# 3. Reverse the entire message

def reverse(x):
    # The -1 step reads the string backward.
    s = x[::-1]
    return s


# 4. Swap the halves, then reverse

def swap_mid_rev(x):
    # First I switch the two halves.
    s_swap = swap_middle(x)

    # Then I reverse the result.
    s = reverse(s_swap)

    return s


# Decode the combined encoding method

def swap_mid_rev_decode(x):
    # I undo the reverse step first.
    s_rev = reverse(x)

    # Then I switch the halves back.
    s = swap_middle(s_rev)

    return s


# 5. Reverse every word separately

def reverse_word(x):
    # Splitting at spaces keeps the words in order.
    words = x.split(' ')
    s = ''

    # I reverse each word but keep the word order.
    for kk in range(len(words)):
        s = s + reverse(words[kk])

        if kk < len(words) - 1:
            s = s + ' '

    return s


# ENCODING METHODS AND THEIR HINTS

#These are the methods we learned in class and I used them.
methods = [
    "even_odd_swap",
    "reverse",
    "reverse_word",
    "swap_middle",
    "swap_mid_rev"
]
#I put guided hints so it is easier to crack the code for the Secret Agent.
#These hints show exactly what happened and how I encoded that message in a different way.
#I think some of my encoded messages are hard to solve, because it is guiding te agent what to do
#So these hints should hopefully help, LOL.
hints = {
    "even_odd_swap": [
        "Look carefully at the positions of the letters.",
        "Characters that belong next to each other may have switched places.",
        "Swap every adjacent pair of characters."
    ],

    "reverse": [
        "The spaces are still in their original positions.",
        "The entire message has been turned around.",
        "Read the complete message from right to left."
    ],

    "reverse_word": [
        "The words are still in the same order.",
        "Look at the letters inside each individual word.",
        "Read each word backward without changing word order."
    ],

    "swap_middle": [
        "The message has been divided into two parts.",
        "The two halves have exchanged places.",
        "Move the second half in front of the first half."
    ],

    "swap_mid_rev": [
        "Two encoding techniques have been combined.",
        "The halves changed places, and the result was reversed.",
        "Reverse the message first, then swap its two halves."
    ]
}


# This function chooses which encoding method to use.

def encode_message(message, method):

    if method == "even_odd_swap":
        return even_odd_swap(message)

    elif method == "reverse":
        return reverse(message)

    elif method == "reverse_word":
        return reverse_word(message)

    elif method == "swap_middle":
        return swap_middle(message)

    elif method == "swap_mid_rev":
        return swap_mid_rev(message)



#SECRET AGENT MESSAGES


# These are the original messages the player must discover.
# I put all my encoding methods into one list so I can easily switch between them when the agent guesses wrong. 
# # Each method has a name and a function that scrambles the message.
#I chose these messages because it helps guide the secret agent what to do in my so called story.
# It was some random phrases that match and then I thought on how to make it harder, so it will be hard to guess. 
# However, some of the encoded ways make it a little easier to guess.
#  If you guys can guess this, its probably because your really good at the secret messages.
#Hopefully, they sound like an actual guided escape room or a spy trying to figure out the stuff, since that was my main goal.

secret_messages = [
    "the final clue is hidden beneath the old clock",
    "trust no signal until the silver lights appear",
    "the missing key unlocks the room behind the library",
    "meet at midnight where the shadows cross",
    "the last agent left a message inside the hollow statue"
]



# START THE GAME


score = 0

print("=" * 55)
print("             SECRET AGENT CODE CRACKER")
print("=" * 55)
print("Decode the hidden messages to complete your mission!")
print("Every wrong guess changes the encoding method.")
print("You have 3 hints for each message.")
print()

for message_number in range(len(secret_messages)):

    answer = secret_messages[message_number]

    # Each new mission starts with a different encoding.
    method_number = message_number % len(methods)

    hints_used = 0
    solved = False

    print("-" * 55)
    print("MISSION", message_number + 1)
    print()

    # The player gets a new encoded version after each mistake.
    while not solved:

        method = methods[method_number]
        secret = encode_message(answer, method)

        print("ENCODED MESSAGE:")
        print(repr(secret))
        print()

        guess = input("Enter the original message: ")
        guess = guess.strip().lower()

        # Check whether the player has cracked the message.
        if guess == answer.lower():
            print()
            print("UR A SMART ONE!")
            print("Secret message decoded successfully!")
            score = score + 1
            solved = True

        else:
            print()
            print("INCORRECT, SECRET AGENT!")

            # Every wrong guess switches to the next method.
            method_number = (method_number + 1) % len(methods)

            # Show a hint for the NEW encoding method.
            if hints_used < 3:
                new_method = methods[method_number]

                print("The encoding method has changed!")
                print("HINT", hints_used + 1, ":",
                      hints[new_method][hints_used])

                hints_used = hints_used + 1

            # After three hints, one final wrong guess fails
            # the mission.
            else:
                print("UR A REALLY BAD SECRET AGENT!")
                print("The original message was:")
                print(answer)
                solved = True

        print()



# FINAL MISSION RESULTS

print("=" * 55)
print("                 MISSION RESULTS")
print("=" * 55)

print("Messages decoded:", score, "out of", len(secret_messages))

if score == len(secret_messages):
    print("YOU ARE A MASTER SECRET AGENT! WHOA UR COOKING")
elif score >= 3:
    print("Nice work, agent! Keep training. You might pass this.")
else:
    print("UR A REALLY BAD SECRET AGENT! You should be fired!!")

print("Thanks for playing!")
print("=" * 55)


# I built this to turn the class project functions into an interactive puzzle game that makes testing more fun.
