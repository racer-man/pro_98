import random
print("Number Guessing Game")
number=random.randint(1, 9)

chances=0
#Starting from 0 give only 5 chances.
while chances < 5:
    guess=int(input("Guess an integer between 1 to 9"))
    if guess == number:
        print("Congrulations You Won!")
        break
    elif guess > number:
        print("Your guess was too low try guess a bigger number", guess)
    else :
        print("Your guess was too high try guess a lower number", guess)
    chances+= 1
if not chances < 5:
    print("All your chances are finished kill this terminal to play again")