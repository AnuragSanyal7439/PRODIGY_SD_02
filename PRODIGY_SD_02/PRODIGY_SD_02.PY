import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Try to guess it, and I'll give you hints!")

    
    random_number = random.randint(1, 100)
    attempts = 0
    guess = 0

    
    while guess != random_number:
        try:
            
            guess = int(input("Enter your guess: "))
            attempts += 1

            
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid integer.")

guess_the_number()
