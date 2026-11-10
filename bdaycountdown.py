
import datetime as dt
import time

# I wanted my project to be more fun than just calculating
# someone's birthday, so I made it into a live countdown and added zodiac info to it!
print('========================================')
print('       MY BIRTHDAY COUNTDOWN!')
print('========================================')
print()


# First, I need the user's birthday to calculate everything else.
# I used a loop so they can try again if they enter an invalid date.
while True:
    try:
        year = int(input('Which year were you born in?\n'))
        month = int(input('Which month (1 for Jan, 2 for Feb, etc.)?\n'))
        day = int(input('Which day in that month?\n'))

        # datetime checks whether the date actually exists.
        date_birth = dt.datetime(year, month, day)

        # A birth date can't be in the future!
        if date_birth.date() > dt.datetime.now().date():
            print("Your birth date can't be in the future. Try again!\n")
        else:
            break

    except ValueError:
        print('That date is not valid. Please try again!\n')


# I made a list because weekday() gives me a number instead of a name.
# Monday is 0, Tuesday is 1, and Sunday is 6.
weekday_names = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
]

print()
print('You may have forgotten which day of the week it was...')
print('But I can tell you! You were born on a ...', end=' ')

weekday_num = date_birth.weekday()
print(weekday_names[weekday_num])
print()


# I added zodiac signs as a bonus to make the project more interesting.
# These are the traditional Western astrology date ranges.
if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = 'Capricorn'
    symbol = 'The Sea-Goat'
    element = 'Earth'
    planet = 'Saturn'
    personality = (
        'Capricorns are often described as ambitious, practical, '
        'and responsible. They like having goals and working hard '
        'to achieve them. They are usually seen as dependable people '
        'who take their responsibilities seriously.'
    )
    strengths = 'Discipline, patience, loyalty, and determination'
    challenges = 'Can be stubborn, overly serious, or too hard on themselves'
    friendship = 'A dependable friend who shows they care through actions'

elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = 'Aquarius'
    symbol = 'The Water-Bearer'
    element = 'Air'
    planet = 'Uranus'
    personality = (
        'Aquarius is associated with originality, independence, '
        'and curiosity. They are often described as people who '
        'think differently and enjoy exploring new ideas. They '
        'may care deeply about making the world a better place.'
    )
    strengths = 'Creativity, open-mindedness, originality, and independence'
    challenges = 'Can seem distant, unpredictable, or overly independent'
    friendship = 'A friend who enjoys interesting conversations and new ideas'

elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = 'Pisces'
    symbol = 'The Fish'
    element = 'Water'
    planet = 'Neptune'
    personality = (
        'Pisces is associated with imagination, empathy, and creativity. '
        'They are often described as thoughtful people who notice '
        'other people’s feelings. They may enjoy art, music, stories, '
        'and expressing themselves in creative ways.'
    )
    strengths = 'Compassion, imagination, intuition, and creativity'
    challenges = 'Can be overly idealistic, sensitive, or indecisive'
    friendship = 'A caring friend who listens and offers emotional support'

elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = 'Aries'
    symbol = 'The Ram'
    element = 'Fire'
    planet = 'Mars'
    personality = (
        'Aries is associated with confidence, energy, and initiative. '
        'They are often described as adventurous people who like '
        'taking on challenges and getting things started. They may '
        'enjoy competition and prefer to act rather than wait.'
    )
    strengths = 'Courage, enthusiasm, leadership, and determination'
    challenges = 'Can be impatient, impulsive, or quick to get frustrated'
    friendship = 'An energetic friend who encourages others to try new things'

elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = 'Taurus'
    symbol = 'The Bull'
    element = 'Earth'
    planet = 'Venus'
    personality = (
        'Taurus is associated with stability, patience, and loyalty. '
        'They are often described as people who appreciate comfort, '
        'familiar routines, and quality time with others. Once they '
        'commit to a goal or relationship, they tend to stick with it.'
    )
    strengths = 'Reliability, patience, loyalty, and persistence'
    challenges = 'Can be stubborn, resistant to change, or possessive'
    friendship = 'A loyal friend who values trust and spending time together'

elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    zodiac = 'Gemini'
    symbol = 'The Twins'
    element = 'Air'
    planet = 'Mercury'
    personality = (
        'Gemini is associated with communication, curiosity, and '
        'adaptability. They are often described as people who enjoy '
        'learning new things, asking questions, and talking about '
        'different topics. They may get bored when life feels repetitive.'
    )
    strengths = 'Communication, adaptability, curiosity, and humor'
    challenges = 'Can become distracted, restless, or indecisive'
    friendship = 'A fun, conversational friend who brings lots of ideas'

elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    zodiac = 'Cancer'
    symbol = 'The Crab'
    element = 'Water'
    planet = 'The Moon'
    personality = (
        'Cancer is associated with caring, intuition, and emotional '
        'connection. They are often described as protective people '
        'who value family, close friendships, and feeling understood. '
        'They may remember meaningful moments and details about others.'
    )
    strengths = 'Empathy, loyalty, thoughtfulness, and protectiveness'
    challenges = 'Can be overly cautious, sensitive, or reluctant to let go'
    friendship = 'A supportive friend who remembers the little things'

elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = 'Leo'
    symbol = 'The Lion'
    element = 'Fire'
    planet = 'The Sun'
    personality = (
        'Leo is associated with confidence, creativity, and generosity. '
        'They are often described as expressive people who enjoy '
        'sharing their talents and encouraging others. They may like '
        'being appreciated and making special moments memorable.'
    )
    strengths = 'Confidence, warmth, creativity, and generosity'
    challenges = 'Can be prideful, attention-seeking, or sensitive to criticism'
    friendship = 'An enthusiastic friend who celebrates others’ successes'

elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = 'Virgo'
    symbol = 'The Maiden'
    element = 'Earth'
    planet = 'Mercury'
    personality = (
        'Virgo is associated with organization, observation, and '
        'problem-solving. They are often described as thoughtful '
        'people who notice details that others might miss. They may '
        'enjoy making plans and finding practical ways to help others.'
    )
    strengths = 'Attention to detail, reliability, helpfulness, and logic'
    challenges = 'Can be overly critical, perfectionistic, or prone to worry'
    friendship = 'A thoughtful friend who offers practical help and advice'

elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    zodiac = 'Libra'
    symbol = 'The Scales'
    element = 'Air'
    planet = 'Venus'
    personality = (
        'Libra is associated with fairness, cooperation, and harmony. '
        'They are often described as people who consider different '
        'points of view and enjoy connecting with others. They may '
        'care about balance, beauty, and making group situations fair.'
    )
    strengths = 'Diplomacy, fairness, cooperation, and social awareness'
    challenges = 'Can be indecisive, conflict-avoidant, or overly concerned with approval'
    friendship = 'A considerate friend who tries to make everyone feel included'

elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    zodiac = 'Scorpio'
    symbol = 'The Scorpion'
    element = 'Water'
    planet = 'Pluto'
    personality = (
        'Scorpio is associated with determination, intensity, and '
        'resourcefulness. They are often described as private people '
        'who value trust and meaningful connections. They may prefer '
        'understanding a situation deeply rather than accepting things '
        'at the surface level.'
    )
    strengths = 'Determination, loyalty, resourcefulness, and focus'
    challenges = 'Can be secretive, suspicious, or reluctant to forgive'
    friendship = 'A devoted friend who values honesty and trust'

else:
    zodiac = 'Sagittarius'
    symbol = 'The Archer'
    element = 'Fire'
    planet = 'Jupiter'
    personality = (
        'Sagittarius is associated with exploration, optimism, and '
        'independence. They are often described as people who enjoy '
        'learning about the world, trying new experiences, and asking '
        'big questions. They may value freedom and expressing opinions.'
    )
    strengths = 'Optimism, curiosity, honesty, and adventurousness'
    challenges = 'Can be impatient, overly blunt, or restless'
    friendship = 'An adventurous friend who enjoys new experiences and big conversations'


# I display the zodiac information in separate sections
# so the user can read their personality profile easily.
print('========================================')
print('          YOUR ZODIAC PROFILE')
print('========================================')
print('Zodiac sign:', zodiac)
print('Symbol:', symbol)
print('Element:', element)
print('Ruling planet:', planet)

print()
print('PERSONALITY')
print(personality)

print()
print('STRENGTHS')
print(strengths)

print()
print('CHALLENGES')
print(challenges)

print()
print('AS A FRIEND')
print(friendship)

print()
print('These descriptions come from traditional Western astrology.')
print('They are for fun and do not determine anyone’s personality!')
print()


# Now I figure out when the next birthday will happen.
current_time = dt.datetime.now()
thisyear = current_time.year

# February 29 needs special treatment because it only exists
# in leap years, so I search for the next actual Feb. 29.
if month == 2 and day == 29:
    birthday_year = thisyear

    while True:
        try:
            thisyear_bday = dt.datetime(birthday_year, 2, 29)

            if thisyear_bday > current_time:
                break

        except ValueError:
            # If this isn't a leap year, I check the next year.
            pass

        birthday_year += 1

    next_bday = thisyear_bday

else:
    # If this year's birthday hasn't happened, I use that date.
    thisyear_bday = dt.datetime(thisyear, month, day)

    if thisyear_bday > current_time:
        next_bday = thisyear_bday
    else:
        # Otherwise, the next birthday is in the following year.
        next_bday = dt.datetime(thisyear + 1, month, day)


# I print the date in a more readable format.
print('Your next birthday will be on ...')
print(next_bday.strftime('%B %d, %Y'))

weekday_num = next_bday.weekday()
print('That will be a ...', weekday_names[weekday_num])
print()


# I calculate the age the user will turn on their next birthday.
age_next_birthday = next_bday.year - year

print('You will be turning', age_next_birthday,
      'on your next birthday!')
print()


# I wanted to add different messages depending on how close
# the birthday is, so the program feels more personal.
dd = next_bday - dt.datetime.now()
days_left = dd.days

print('========================================')
print('          BIRTHDAY MESSAGE')
print('========================================')

if days_left > 30:
    print('The countdown begins! Your birthday is coming!')
elif days_left > 7:
    print('Your birthday is getting closer!')
elif days_left > 1:
    print("It's almost birthday week! Get excited!")
elif days_left == 1:
    print('OMG! Your birthday is TOMORROW!')
else:
    print('Your birthday is almost here!')

print()


# This is the main part of my project!
# The loop keeps checking the time until the next birthday.
while True:
    current_time = dt.datetime.now()
    dd = next_bday - current_time

    # When the timer reaches zero, the birthday celebration starts.
    if dd.total_seconds() <= 0:
        print('\nHAPPY BIRTHDAY!!!')
        break

    # I get the number of complete days and leftover seconds.
    days_left = dd.days
    total_seconds_left = dd.seconds

    # I split the seconds into hours, minutes, and seconds.
    total_mins_left, seconds_left = divmod(total_seconds_left, 60)
    hrs_left, minutes_left = divmod(total_mins_left, 60)

    # I calculate complete calendar months instead of assuming
    # that every month has exactly 30 days.
    months_left = (
        (next_bday.year - current_time.year) * 12
        + next_bday.month - current_time.month
    )

    # Some months don't have the same number of days.
    # I adjust the date until it becomes a valid calendar date.
    while months_left > 0:
        target_month = current_time.month + months_left
        target_year = current_time.year

        while target_month > 12:
            target_month -= 12
            target_year += 1

        target_day = current_time.day

        while target_day > 0:
            try:
                month_date = current_time.replace(
                    year=target_year,
                    month=target_month,
                    day=target_day
                )
                break
            except ValueError:
                target_day -= 1

        # I don't count a month if its date goes past the birthday.
        if month_date <= next_bday:
            break

        months_left -= 1

    # I find the date after adding the complete calendar months.
    if months_left > 0:
        target_month = current_time.month + months_left
        target_year = current_time.year

        while target_month > 12:
            target_month -= 12
            target_year += 1

        target_day = current_time.day

        while target_day > 0:
            try:
                month_date = current_time.replace(
                    year=target_year,
                    month=target_month,
                    day=target_day
                )
                break
            except ValueError:
                target_day -= 1
    else:
        month_date = current_time

    # I subtract the calendar-month date to find the remaining days.
    remaining_time = next_bday - month_date
    remaining_days = remaining_time.days

    # I turn those remaining days into weeks and extra days.
    weeks_left = remaining_days // 7
    extra_days = remaining_days % 7

    # I use end='\r' to keep updating the countdown on one line.
    print(
        'Time until your birthday:',
        months_left, 'months,',
        weeks_left, 'weeks,',
        extra_days, 'days,',
        hrs_left, 'hours,',
        minutes_left, 'minutes,',
        seconds_left, 'seconds.       ',
        end='\r'
    )

    # Waiting one second makes the countdown update every second.
    time.sleep(1)
