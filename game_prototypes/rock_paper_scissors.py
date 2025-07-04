import random

choices = ["rock", "paper", "scissors"]

def main():
    while True:
        user = input("Rock, paper, or scissors? (q to quit) ").lower()
        if user == 'q':
            print("Bye!")
            break
        if user not in choices:
            print("Invalid choice.")
            continue
        computer = random.choice(choices)
        print("Computer chose:", computer)
        if user == computer:
            print("Tie!")
        elif (user=='rock' and computer=='scissors') or \
             (user=='paper' and computer=='rock') or \
             (user=='scissors' and computer=='paper'):
            print("You win!")
        else:
            print("You lose!")

if __name__ == '__main__':
    main()
