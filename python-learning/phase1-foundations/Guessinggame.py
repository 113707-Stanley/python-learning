print(f"\nWelcome to the Guessing Game!")
secret_number = 25
max_attempts = 5
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"\nAttempt {attempt}/{max_attempts}: Guess the secret number. Enter a number below 50: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number!")
        break
else:
    print(f"\n Sorry, you've used all your attempts. The secret number was {secret_number}.")   

