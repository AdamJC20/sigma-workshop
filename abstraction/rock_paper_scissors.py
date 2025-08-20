import random


def pick_random_move() -> str:
    """Gives a random RPS choice"""

    return random.choice(["rock", "paper", "scissors"])


def player_wins(player_choice: str, comp_choice: str) -> bool:
    """Returns True if player_choice beats comp_choice"""
    winner_dict = {"rock": "scissors",
                   "paper": "rock",
                   "scissors": "paper"}
    return winner_dict[player_choice] == comp_choice


def validate_input(input) -> bool:
    return input.lower() in ["rock", "paper", "scissors"]


def get_player_choice() -> str:
    """Receives and returns player's choice"""
    while True:
        choice = input(
            "Enter your choice (\"rock\", \"paper\" or \"scissors\"): ")
        if validate_input(choice):
            return choice.lower()

        else:
            print("Invalid input")


def play_rock_paper_scissors() -> None:
    """Runs a game of rock paper scissors"""
    player_choice = get_player_choice()
    comp_choice = pick_random_move()
    if player_wins(player_choice, comp_choice):
        print(f"You win! Computer chose {comp_choice}.")

    else:
        print(f"You lose! Computer chose {comp_choice}.")


play_rock_paper_scissors()
