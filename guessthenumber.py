n = 18

print("\t \t \t \t Guessing Game \n")

no_guess = 0
no_try = 5

print("You have 5 chances \n")


while(no_guess < no_try):

    Guess = int(input("Guess the no:"))


    if Guess == n:
        print("You won this game in the" , no_guess + 1,"chance" )
        break

    if Guess > 30:
        print("Write the number smaller than 30 \n")

    elif(Guess <= 10):
        print("Increase your number")

    elif(Guess >= 19):
        print("Decrease your number")

    elif (Guess >= 10 and Guess < n) :
        print("Little increase your number")

    else:
        print("Your number is decimal or a negative integer ")


    print("Guess:",no_guess + 1,"\n")

    no_guess = no_guess + 1

