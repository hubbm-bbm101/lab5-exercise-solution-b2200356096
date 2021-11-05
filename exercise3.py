from random import randint
number = randint(0,100)
your_guess = None
while your_guess != number:
    your_guess = int(input("Enter your guess:"))
    if (your_guess == number):
        break
    if (your_guess <= number):
        print("Increase your number")
    if (your_guess >= number):
        print("Decrease your number")
print("You won!!")