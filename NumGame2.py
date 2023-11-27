import random

upper_range = input("please enter the Maximum number for our game : ")
lower_range = input("please enter the minimum number for our game : ")


if upper_range:
    print(upper_range)
    upper_range = int(upper_range)

    if upper_range <= 0:
        print("Larger Number Than '0' : ")

else:
    print("Please enter Number: ")
    
if lower_range:
    print(lower_range)
    lower_range = int(lower_range)

    if lower_range <= 0:
        print("Larger Number Than '0' : ") 

else:
    print("Please enter Number: ")

randam_nu =  random.randint(lower_range, upper_range)
guesess = 0

while True:
    guesess +=1
    guess = input("Make a guess : ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("type a number: ")
        continue

    if guess == randam_nu:
        print("You Got correct : " )
        break

    elif guess > randam_nu:
        print("you guess its above nomber :")

    else:
        print("you guess its below nomber :")

print("you got it in ", guesess, "guesess")