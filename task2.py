import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        # Increment attempt count
        attempts += 1
        try:
            # Ask user for their guess
            guess = int(input("Enter your guess: "))

            # Compare the guess to the generated number
            if guess < number_to_guess:
                print("Too low, try again!")
            elif guess > number_to_guess:
                print("Too high, try again!")
        except ValueError:
            # Handle non-integer input
            print("Please enter a valid number.")

    # When the correct number is guessed
    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

# Run the game
if __name__ == "__main__":
    guessing_game()
