"""Unit tests for rock_paper_scissors.py"""


from rock_paper_scissors import player_wins, get_player_choice


""""Tests for player_wins"""


def test_player_wins_valid_1():
    assert player_wins("rock", "scissors") == True


def test_player_wins_valid_2():
    assert player_wins("paper", "scissors") == False


def test_player_wins_valid_3():
    assert player_wins("rock", "paper") == False


def test_player_wins_invalid_1():
    assert player_wins(
        "lizard", "spock") == "Error, one or both choices are invalid"


"""Tests for """


def test_get_player_choice_1():
    assert get_player_choice() in ["rock", "paper", "scissors"]
