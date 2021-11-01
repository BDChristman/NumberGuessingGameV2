# Brian D. Christman
# Purpose: to generate a random integer between 1 and 100 and allow a named user to try and
# guess the number. The number of guesses are counted and printed once the game is complete.
# The top five game scores are also tracked and printed at the completion of each game.
# The player has the option of repeating the game without stopping the program.

# Import the package used in this program
import random

# Begin the try block for error management and the while loop that allows the player to keep playing
# until they wish to stop
try:
    while True:
        # Generate and print a random integer between 1 and 100
        correctNumber = random.randint(1, 101)
        # print(correctNumber)  # Uncomment to validate that the program is working properly

        # Allow the player to enter their name and if they don't enter a name, repeat the entry process
        name = input("Please enter your name to begin the game: ")
        print()
        while True:
            if name == "":
                print("The name you have entered is invalid, please try again.")
                name = input("Please enter your name to begin the game: ")
                print()
            else:
                break

    # Print the introduction and rules to the number guessing game
        print("Welcome to the number guessing game!")
        print("To play, enter an integer between 1 and 100 (no decimals) in the guess prompt.")
        print("To stop, enter 'stop' in the guess prompt.")
        print()

    # Create the guess counter, stop options, and try block and ask for the first guess from the user
        try:
            guessCtr = 0
            stop = ['stop', 'Stop', 'STOP']
            number = input("Please enter your number guess (an integer between 1 and 100): ")

        # Assess the user's input and print out whether the guess was valid and increment the counter
        # or have the user guess again or stop. Stop the game and print the number of guesses made
        # if the user guesses correctly.
            while True:
                if number in stop:
                    guessCtr = 1000
                    break
                elif not number.isnumeric():
                    print("You have not entered an integer between 1 and 100. This guess did not count.\n")
                    number = input("Please enter your number guess (an integer between 1 and 100): ")
                elif int(number) not in range(1, 101):
                    print("You have not entered an integer between 1 and 100. This guess did not count.\n")
                    number = input("Please enter your number guess (an integer between 1 and 100): ")
                elif int(number) < correctNumber:
                    print("Your guess is too low.\n")
                    guessCtr = guessCtr + 1
                    number = input("Please enter your number guess (an integer between 1 and 100): ")
                elif int(number) > correctNumber:
                    print("Your guess is too high.\n")
                    guessCtr = guessCtr + 1
                    number = input("Please enter your number guess (an integer between 1 and 100): ")
                else:
                    print("Your guess is correct! Congratulations!")
                    guessCtr = guessCtr + 1
                    print(f"It took you {guessCtr} guesses to pick the correct number!\n")
                    break

        # Check for errors and print if an error occurred
        except Exception as e:
            print("An error has occurred.")
            print(e)

        # Create a list for holding lists from the text file
        scoresList = []

        # Open, read, and clean the text file for use in Python
        # Store the file information (line by line) in a list of lists for easier sorting
        # Check for errors with the text file
        try:
            with open('topPlayers.txt', "r") as scoresFile:
                for line in scoresFile.readlines():
                    scores = line[0:9].rstrip().lstrip()
                    playerName = line[10:].rstrip().lstrip()
                    scoresTempList = [int(scores), playerName]
                    scoresList.append(scoresTempList)
            scoresFile.closed
        except Exception as e:
            print(f"There is something wrong with the text file you are trying to read.")
            print(f"\t{e}")

        # Add the current players score and name, then sort the dataset by score
        playerInfo = [int(guessCtr), name]
        scoresList.append(playerInfo)
        scoresList.sort(key=lambda x: (x[0]))
        scoresList.pop(5)

        try:
            # Write a new text file, line by line, of the sorted data
            ctr = 0
            with open('topPlayers.txt', 'w') as newScores:
                while ctr < len(scoresList):
                    newScores.write('{:<9} {:<10}\n'.format(str(scoresList[ctr][0]), scoresList[ctr][1]))
                    ctr = ctr + 1
            newScores.close()

            # read the new text file and print the current leaderboard
            leaderboard = open('topPlayers.txt', 'r')
            leaders = leaderboard.read()
            print("Current Leaderboard")
            print(leaders)
            leaderboard.close()
        except Exception as e:
            print(f"Something went wrong when making the leaderboard. Invalid entries are being used.")

        # Ask if the player would like to play again and either loop through the program again or break
        play = ["yes", "Yes", "YES", "y", "Y", "ye", "YE", "Ye"]
        restart = input("Would you like to play again (enter 'yes', if you do): ")
        if restart not in play:
            break
        else:
            print()
            continue

# Check for any major game breaking errors. And let the player know if there are.
except Exception as e:
    print(f"Something went terribly wrong with the program and caused it to crash. Please play again.")


# Print the closing statement of the game and stop the program.
finally:
    print(f"Thank you for playing the number guessing game!")
