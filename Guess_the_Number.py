import random


def main():

    player_name = input("Hello What is your name?: ")

    print(f"Well {player_name}, I am thinking of a number between 1 and 20\nTake a guess.")

    guesses_taken = 0
    number_guessed = False
    number = random.randint(1, 20)

    while not number_guessed:
        guess = input()
        try:
            guess = int(guess)
            if guess > 20 or guess < 1:
                print("Invalid. Please input a number between 1 and 20")
                pass
            elif guess > number:
                guesses_taken += 1
                print("Lower")
            elif guess < number:
                guesses_taken += 1
                print("Higher")
            elif guess == number:
                guesses_taken += 1
                print(f"You got it! It took {guesses_taken} guesses.")
                number_guessed = True
                break
        except ValueError:
            print("Try again, Enter a Number between 1 and 20")


main()
