import time
print('Hello World')










# Get player name



playername = input('What is your name?')
city = input('What city are you from? ')
favoritecolor = input('What is your favorite color? ')

# Creative greeting
print('\n')
print('Loading your profile', end='')

for i in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)

print('\n')

print(f'Hello {playername}!')
print(f'Welcome from {city}!')
print(f'Your favorite color is {favoritecolor}!')


# Escape sequence examples
print('\nSpecial Characters Demo:')
print('Quote: \"Python is awesome!\"')
print('Backslash: \\')
print('Tab:\tWOW')
print('Vertical Tab:\vCool!')


print()
print()
print()
print('1234')

print('PPPPP', 'Y   Y', 'TTTTT', 'H   H', 'OOOOO', 'N   N', sep = '  # ')
print('P   P', ' Y Y ', '  T  ', 'H   H', 'O   O', 'NN  N', sep = '  # ')
print('PPPPP', '  Y  ', '  T  ', 'HHHHH', 'O   O', 'N N N', sep = '  # ')
print('P    ', '  Y  ', '  T  ', 'H   H', 'O   O', 'N  NN', sep = '  # ')
print('P    ', '  Y  ', '  T  ', 'H   H', 'OOOOO', 'N   N', sep = '  # ', end= ' ')
print('is so cool')

print('\n')

# Dynamic name art using loops
print('Your name in cool style:\n')

for letter in playername.upper():
    print(letter * 5)
    time.sleep(0.2)

# Countdown using time module
print('\nLaunching Python Power Mode!')

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print('🚀 GO!')

# Carriage return demo
print('\nProgress:')
for i in range(101):
    print(f'\r{i}% Complete', end='')
    time.sleep(0.02)

print('\n')

# Fun personalized message
print(f'{playername} from {city} who likes {favoritecolor} is learning Python like a pro!')
