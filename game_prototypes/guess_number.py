import random

def main():
    target = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        attempts += 1
        if guess == target:
            print(f"Correct! Attempts: {attempts}")
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")

if __name__ == "__main__":
    main()
