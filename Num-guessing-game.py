import random

print("Number guessing game")
print("Guess a random number between 1 & 9")
number = random.randint(1,9)
chances = 5
guess = input("Enter your guess ")

while chances < 5 :
    if guess > 5 : 
        print("Your guess was too high !")
        print("Guess a number lower than " + guess)
    elif guess < 5:
        print("Your guess was too low !")
        print("Guess a number higher than " + guess)
if guess == number :
    print("CONGRATS ! YOU WON !")