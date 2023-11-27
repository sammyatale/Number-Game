import random

upper_range = input("Please enter the Maximum number for our game: ")
lower_range = input("Please enter the minimum number for our game: ")

if upper_range:
    print(upper_range)
    upper_range = int(upper_range)

    if upper_range <= 0:
        print("Enter a larger number than '0': ")

else:
    print("Please enter a number: ")

if lower_range:
    print(lower_range)
    lower_range = int(lower_range)

    if lower_range <= 0:
        print("Enter a larger number than '0': ") 

else:
    print("Please enter a number.")

random_num =  random.randint(lower_range, upper_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Type a number: ")
        continue

    if guess == random_num:
        print("You guessed correctly.... ")
        break
    elif guess > random_num:
        print("Your guess is above the number... ")
    else:
        print("Your guess is below the number... ")

print("You got it in", guesses, "guesses.")
