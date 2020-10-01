# this is the same code but its simplified and its easy for other coders to read
# you have used a lot of elif which is reduced

n = 18
attempts = 1

while (attempts <= 9):
    try:
        inp = int(input("Enter your number\n"))

        if inp > n:

            print("Enter a lesser number\n")


        elif inp < n:

            print("Enter a greater number\n")


        else:
            print("you win")
            print("you finished the game in", attempts, "attempts")
            break

        print(9 - attempts, "no. of guesses left")
        attempts = attempts + 1

        if attempts > 9:
            print("game over")

        if attempts == 9:
            print("Hint : Number is between 15 to 20")
    except ValueError:
        print("Enter a Integer only")

