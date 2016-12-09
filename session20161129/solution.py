from random import randint


def guessNumber():
    """
    This is function that prompts the user to guess a number between 1 and 20
    It also gives helpful clues as to the what to guess
    """
    random_number = randint(1, 20)
    print("random - ", random_number)

    guessed_right = False

    while not guessed_right:
        try:
            guessed_number = int(input("Please enter a number between 1 and 20: "))

        except ValueError:
            print("Please make sure you enter a valid number")
            continue


        if guessed_number > 20 or guessed_number < 0:
            print("Please make sure you enter a number between 1 and 20")
        else:
            if guessed_number == random_number:
                print("Yay! you guessed correctly")
                guessed_right = True

            elif guessed_number < random_number and guessed_number != 0:
                print("Too low, guess higher or enter 0 to quit")

            elif guessed_number > random_number and guessed_number != 0:
                print("Too high, guess lower or enter 0 to quit")

            elif guessed_number == 0:
                print("You have decided to quit, thanks for playing")
                break




if __name__ == "__main__":
    guessNumber()