"""paper, rock, scissors game."""
import random


def get_user_choice() -> str:
    """Get the user's choice."""
    choices = ['paper', 'rock', 'scissors']
    choice = input("Enter your choice (paper, rock, scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (paper, rock, scissors): ").lower()
    return choice


def get_computer_choice() -> str:
    """Randomly select the computer's choice."""
    choices = ['paper', 'rock', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice: str, computer_choice: str) -> str:
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Paper, Rock, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()