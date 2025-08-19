"""Mediocre Wordle Clone"""

import random


def check(correct_word, guess):
    """Check guess against correct word"""
    result = ['_' for _ in range(len(correct_word))]
    for pos, letter in enumerate(guess):
        if letter == correct_word[pos]:
            result[pos] = letter

        elif letter in correct_word:
            result[pos] = '?'

    return result


def generate_word(word_list):
    """Grab random word from word list"""
    return random.choice(word_list)


def run_game(word_list):
    """Run the game"""
    correct_word = generate_word(word_list)
    go = 5
    while go > 0:
        input1 = input("Enter your guess: ")
        if len(correct_word) != 5:
            print("Please enter a 5-letter word.")
            continue

        result = check(correct_word, input1)
        print(' '.join(result))
        if input1 == correct_word:
            print("Congratulations! You've guessed the word.")
            return

        go -= 1
    print(f"Sorry, you didn't guess the word. The word was {correct_word}.")


list2 = ["apple", "place", "grape", "chair", "spear", "green",
         "plant", "house", "water", "money", "tiger", "panda"]

run_game(list2)
