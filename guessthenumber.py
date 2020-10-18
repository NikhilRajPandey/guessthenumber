# this is the same code but its simplified and its easy for other coders to read
# you have used a lot of elif which is reduced
#Importing Random Module

import random

n = random.randint(1,20)

attempts = 1

while attempts <=9:

    try:

        inp = int(input("Guess Any number between 1 to 20\n"))

        if inp > n:

            print("Enter a lesser number\n")

        elif inp < n:

            print("Enter a greater number\n")

        else:

            print("you win")

            print(f"you finished the game in {attempts} attempts")

            break

        print(f"{9 - attempts} no. of guesses left")

        attempts = attempts + 1

        if attempts > 9:

            print("game over")

        if attempts == 9:

            print(f"Hint : Number is between {n-3} to {n+1}")

    except ValueError:

        print("Enter a Integer only")

