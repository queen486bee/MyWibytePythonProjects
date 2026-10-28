# OPERATION MIDNIGHT: CRACK THE ENEMY CODE

import random

letters = 'abcdefghijklmnopqrstuvwxyz'


# I switch the letters in each pair to scramble the message.
def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ''

    for i in range(len(even_letters)):
        s = s + odd_letters[i]
        s = s + even_letters[i]

    return s


# I reverse the entire message, including its spaces.
def reverse(x):
    return x[::-1]


# I split the message in half and switch the two halves.
def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '

    first_half = x[0:int(len(x) / 2):1]
    second_half = x[int(len(x) / 2)::1]

    return second_half + first_half


# This is my Caesar cipher. It shifts every letter by a key.
def caesar_cipher(x, n):
    s = ''

    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx + n) % 26
            s = s + letters[new_idx]

    return s


# ------------------------------------------------------------
# MISSION BRIEFING
# ------------------------------------------------------------

print()
print("=" * 48)
print("       OPERATION MIDNIGHT")
print("          TOP SECRET")
print("=" * 48)
print("Agent, we intercepted an enemy transmission!")
print("Crack the code before the enemy escapes.")
print()

# These are themed passwords instead of totally random letters.
# I made them exactly 10 letters long to match the assignment.
secret_codes = [
    'dragonfire',
    'starhunter',
    'firewizard',
    'darkmatter',
    'moonwalker',
    'nightblade'
]

# The enemy randomly chooses one password for this mission.
secret_code = random.choice(secret_codes)

# The enemy hides this special header inside the message.
header = 'python'

# I hide the header at a random position in the password.
# This means it won't always be at the beginning!
header_position = random.randint(0, len(secret_code))

msg = (secret_code[:header_position]
       + header
       + secret_code[header_position:])


# ------------------------------------------------------------
# ENEMY ENCODING
# ------------------------------------------------------------

# The enemy can leave the message alone or use one of
# the three scrambling methods we learned in class.
encoders = [
    ("No extra scrambling", None),
    ("Even-Odd Letter Swap", even_odd_swap),
    ("Reverse the Whole Message", reverse),
    ("Swap Middle Halves", swap_middle)
]

encoder_number = random.randint(0, len(encoders) - 1)
encoder_name, encoder_function = encoders[encoder_number]

if encoder_function == None:
    msg_enc = msg
else:
    msg_enc = encoder_function(msg)

# The enemy adds another layer using a random Caesar key.
# The key is different each time the program runs.
caesar_key = random.randint(1, 25)
msg_enemy = caesar_cipher(msg_enc, caesar_key)

print("INCOMING ENEMY TRANSMISSION:")
print()
print(msg_enemy)
print()
print("Scrambling method: UNKNOWN")
print("Caesar cipher key: UNKNOWN")
print()
print("Cracking the transmission...")
print()


# ------------------------------------------------------------
# CRACK THE CODE
# ------------------------------------------------------------

code_cracked = False

# I test every possible Caesar key until I find the right one.
for kk in range(1, 26):

    # Shifting backwards undoes the enemy's Caesar cipher.
    msg_dec = caesar_cipher(msg_enemy, -kk)

    # I test all four possible ways the enemy could have
    # scrambled the message before applying the Caesar cipher.
    possible_messages = [
        ("No extra scrambling", msg_dec),
        ("Even-Odd Letter Swap", even_odd_swap(msg_dec)),
        ("Reverse the Whole Message", reverse(msg_dec)),
        ("Swap Middle Halves", swap_middle(msg_dec))
    ]

    # I check each possible decoded message for the header.
    for method_name, candidate in possible_messages:

        if header in candidate:

            # The header tells me where the secret code is hidden.
            # I remove only the first occurrence of 'python'.
            secret_found = candidate.replace(header, '', 1)
            print("=" * 48)
            print("       TRANSMISSION CRACKED!")
            print("=" * 48)
            print("Enemy header:", header)
            print("Caesar key discovered:", kk)
            print("Encoding method:", method_name)
            print("Enemy password:", secret_found)
            print()
            print("MISSION STATUS: SUCCESS!")
            print("The enemy's secret has been discovered!")
            print("Great work, Agent. Operation Midnight is complete!")

            code_cracked = True

            # I stop checking other encoding methods after success.
            break

    # I also stop testing Caesar keys once the message is cracked.
    if code_cracked:
        break


# This is the backup ending in case no solution is found.
if not code_cracked:
    print("MISSION FAILED!")
    print("The enemy escaped. Try again, Agent!")

print()
print("          END OF MISSION")
