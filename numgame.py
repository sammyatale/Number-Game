import random

top_of_range = input("type of number: ")

if top_of_range:#.isdigit():
    #top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type number larger than 0')
        quit()

else:
    print('please type a number: ')
    quit()

#low_of_range = input("type a number: ")

random_number = random.randint(0, top_of_range)
#print(random_number)
guesess = 0

while True:
    guesess +=1
    guess = input('make a guess: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a Number: ")
        continue

    if guess == random_number:
        print("You got it correct :  ")
        break
    elif guess > random_number:
        print("you are above the number: ")
    else:
        print("you are below the number: ") 

print("You got it in ", guesess, "guesess")