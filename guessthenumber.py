"""
Guess The Number (game, python)

This script file is written in python3. This script features a game in which we have to guess the random number that is selected by the computer in the range 1-20. Then, we are provided a limited time to guess that number, also we get hints as per we get in the way answering the questions. We are also limited by our number of attempts.

Author : 
Started on : 

Last modified : May 1, 2021
Done by : Rishav Das (https://github.com/rdofficial/)

Contributors on this project (Add your name if you ever gave something to this script file, do it honestly) :
1.
2. Rishav Das (github:https://github.com/rdofficial, email:rdofficial192@gmail.com)
"""

# ----
# Update by : Rishav Das (https://github.com/rdofficial/)
#
# Changes made :
# [1] Added more comments in order to make the .py file more clearly readable to beginners as well as other users. Also changing some variable names to more meaningful versions of them.
# [2] Added the colored output feature for the linux users, thus making the game look more better.
# [3] The loose way of coding for making it easy to read is still maintained and is not disturbed.
# [4] Added code for making the script work more error free and even added code for making it better.
# ----

# Importing random module
#
# We here require the function 'randint' from the random module. We will use the function to get a random number between 1 to 20.
import random

computerChoosedNumber = random.randint(1, 20)

attempts = 1

while attempts <=9:
    # Executing the loop of asking the user to enter a number only for nine times (nine attempts)

    try:
        # Asking the user to guess any random number ranging between 1 to 20
        userEnteredNumber = int(input('Guess any number between 1 to 20 : '))

        if userEnteredNumber > computerChoosedNumber:
            # If the user entered number is greater than the computer choosed number

            print('[ The entered number is greater than the actual number, choose something lesser than this ]\n')

        elif userEnteredNumber < computerChoosedNumber:
			# If the user entered number is lesser than the computer choosed number

            print('[ The entered number is lesser than the actual number, choose something greater than this ]')

        else:
            # If the user entered number matches the computer choosen number, then we exit the game displaying the win message to the user

            print('\n[ YOU WON : You finished the game in {} attempts ]'.format(attempts))

            break

        # If the user entered number did not matches with the computer choosen number, then we proceed from here
        print("[ Only {} out of 9 attempts are left ]".format(9 - attempts))

        attempts = attempts + 1  # Ascening the number of attempts that are used by the user

        if attempts > 9:
            # If the number of the attempts attempted by the user excedes 9, then we finish the game here

            print('[ GAME OVER ]')

            if attempts == 9:
                # If now the next attempt for the user is the 9th attempt, then we give a hint to the user for guessing the number

                print('[ Hint : Number is between {} to {} ]'.format(n - 3, n + 1))

    except ValueError:
        # If the user entered number isn't a number actually, then we encounter this error and thus we display the error message to the user

        print('[ Error : Please enter a numeric value only ]')

    except KeyboardInterrupt:
        # If the user presses the CTRL+C key combo, then we quit the script

        input('[ QUITING ]\nPress enter key to continue...')
        quit()

    except Exception as e:
        # If there are more errors encounterd during the process, then we display the error message to the user

        print('[ Error : {} ]'.format(e))
        quit()

# This "Press enter key to continue..." is for preventing the sudden stopping of execution of the script
input('Press enter key to continue...')
