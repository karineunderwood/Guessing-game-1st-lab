"""A number-guessing game."""

# Put your code here
import random


print("hi")
users_name = input("Howdy, what's your name? ")
print(f"{users_name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.")
guesses = 0
secret_num = random.randint(1, 100)
while True:
    guess = int(input("Your guess: "))
    if guess < secret_num:
        print(f"The number {guess} is too low!")
        guesses += 1
    elif guess > secret_num:
        print(f"The number {guess} is too high!")
        guesses += 1
    else:
        print(f"Congrats, {users_name}! You found my number in {guesses} tries!")
        break
