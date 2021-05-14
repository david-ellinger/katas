import random

RULES = {
    "ROCK": {"SCISSORS": True, "ROCK": False, "PAPER": False},
    "PAPER": {"SCISSORS": False, "ROCK": True, "PAPER": False},
    "SCISSORS": {"SCISSORS": False, "ROCK": False, "PAPER": True},
}


def main():
    raw_choice = input("Rock, Paper or Scissors\n")
    choice = raw_choice.upper()
    if choice != "ROCK" and choice != "SCISSORS" and choice != "PAPER":
        print("Invalid selection")
        return
    opponent_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
    print(f"Your choice: {choice}. Opponent choice: {opponent_choice}")
    win = RULES[choice][opponent_choice]
    if win:
        print("You win the game")
    elif choice == opponent_choice:
        print("The game was a tie")
    else:
        print("You did not win the game")


if __name__ == "__main__":
    main()
