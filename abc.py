import random

def number_guessing_game():
    print("Welcome Player....\nThe Game has been started....")

    Min = int(input("Enter the lower value of the range: "))
    Max = int(input("Enter the upper value of the range: "))

    if Min >= Max:
        print("Invalid range. The maximum value must be greater than the Minimum value.")
        return

    number = random.randint(Min, Max)
    chances = 5


    print(f"You have total {chances} chances to guess the correct number to win the game.")

    for attempt in range(1, chances + 1):
        guess = int(input(f"Attempt {attempt}:\nYour guessed number is: "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct which is {number}...")
            break
    else:
        print(f"You have used all your chances.\nThe correct number is {number}...")
number_guessing_game()
