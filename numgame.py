import random

top_of_range = input("Type of number:- ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type number larger than 0.')
        quit()

else:
    print('Please type a number.')
    quit()

#low_of_range = input("type a number: ")

random_number = random.randint(0, top_of_range)
#print(random_number)
guesess = 0

while True:
    guesess +=1
    guess = input('Make a guess:- ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a Number.")
        continue

    if guess == random_number:
        print("You got it correct.")
        break
    elif guess > random_number:
        print("You're guess is greater than randomly generated number.")
    else:
        print("You're guess is smaller than randomly generated number.") 

print("You got it in ", guesess, "guesess")
