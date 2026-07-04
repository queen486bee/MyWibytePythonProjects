# Initial Intro
print("Welcome to the best business around the world! Would you want to come inside?")

#answer = input("Tell a word\n")
#print(answer, 'apple', sep='')
#print(answer.strip(), 'apple', sep='')

answer = input("Enter: password, to come inside.\n")

if answer.lower() == "password":
    print("Welcome!")
else:
    print("Denied entry. Come again later")
    exit()

#This exit is used so that the user can't move onto the next steps since they didn't enter the password right. If I don't put the exit there, then the user will be answering the following questions even if they are not supposed to do that.

print("So you want to meet the CEO ???")
print("I am his assistant")
print("First you have to pass this quiz")
print("The CEO is very busy, and probably doesn't want to see you")
print("I think you are going to fail this")
print(); 

answer = input("ok, tell me what action words are called in English?\n")

if answer.lower() == "verbs":
    print("Correct, but that was only a warm up ...")
else:
    print("How can you be this stupid? ... your chances of meeting the CEO are very low")  
print()

answer = input("alright, what type of words decribe nouns and what type describe verbs, respectively? Answer with ',' no spaces, in between them.?\n")

if answer.lower() == "adjectives,adverbs":
    print("Correct...")
else:
    print("This is not tuff, you got it wrong. Lock in...")  
print()

#Moving onto the next question

answer = input("Give me an 8 letter English word with at least 3 vowels\n")
if len(answer) == 8:
    print("Your word has 8 letters ...")
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')
    
    count_vowels = count_a+count_e+count_i+count_o+count_u 
    if count_vowels > 3:
        print("Oof ... you gave me more than 3 vowels")
        print("You are wasting my time, I needed only 3.")
    elif count_vowels < 3:
        print("that had less than 3 vowels")
        print("You tried to act smart, but I caught you.")
    else:
        print("What ... exactly 3 vowels ...")
        print("You are not motivated, you are not putting any extra effort")
else:
    print("You seem to be a disaster.")
    print("That word did not even have 8 letters.")


#Next question

print()
sentence = input("ok, tell me a sentence ending in 'wise assistant' (no question please)\n")
# print(sentence.endswith('wise assistant.'))
if sentence.endswith('wise assistant'):
    print("Haven't you learnt about punctuations?")
elif sentence.endswith('wise assistant.'):
    len_first = sentence.find(' ')
    if len_first < 5:
        print("The first word in the sentence is too short.")
else:
    print("I really think you will make the CEO furious.")


print()   
print("Ok, pick your preferred appointment time for next Tuesday(A/B/C/D)")
print("A. 14 mins past midnight", "B. 36 mins before sunrise", sep='\t'); 
print("C. 25 mins before noon", "D. 48 mins after sunset", sep='\t');
appointment = input('Select your slot (A/B/C/D)\n')

if appointment == 'A':
    print("Careful, CEO may be sleepy.")
elif appointment == 'B':
    print("Warning, CEO may be jogging.")
elif appointment == 'C':
    print("Beware, CEO may be hungry.")
else:
    print("Caution, CEO may be tired.")

print("You are cooked either way, whatever appointment you choose.")
print()
print("Good luck for your appointment, bye for now!")
print("I know you are going to fail.")
