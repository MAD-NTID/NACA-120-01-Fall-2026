
"""
@author: <Your name>
date: <Today's date>
Project Code Name: HandBattle
Purpose:
    A program that plays Morra
"""

import datetime
import random

# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
LINE_SEPARATOR = "=============================="
HAND_MIN = 1
HAND_MAX = 3

"""
    This function will print the header containing 
    the game name, version number, and today's date and time
"""


def get_game_header():
    now = datetime.datetime.now()

    return \
        f"{LINE_SEPARATOR}" \
        "\nMorra" \
        "\n\tGame Version 1.0" \
        f"\n{LINE_SEPARATOR}" \
        f"\nDate and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"


"""
    This function generates XP.
    It generates a random XP value and multiples it by the current round number

    Parameter:
        game_round: The current round in the game

    Returns:
        The XP earne for the round
"""


def generate_xp(game_round):
    if game_round < 1:
        game_round = 1

    return random.randint(HAND_MIN, HAND_MAX) * game_round


"""
    This function will randomly pick a hand for the computer.
    This will return a hand from HAND_MIN (1) to HAND_MAX (3)
"""


def get_computer_hand():
    return random.randint(HAND_MIN, HAND_MAX)


"""
    This function randomly generates the computer's guess.
    The guess will be between HAND_MIN * 2 and HAND_MAX * 2.
"""


def get_computer_guess():
    return random.randint(HAND_MIN, HAND_MAX) + random.randint(HAND_MIN, HAND_MAX)
# PREDEFINED ABOVE, DO NOT MODIFY ANY CODE


# STUDENT CODE HERE
# Declare and implement the five required functions below.
# Refer to the README.md for function names, parameters and expected return values
def determine_winner(player_hand, player_guess, computer_hand, computer_guess):
    combined_hand = player_hand + computer_hand

    # Evaluate Tie first - important
    if player_guess == combined_hand and computer_guess == combined_hand:
            return "tie"
    elif player_guess == combined_hand:
        return "player"
    elif computer_guess == combined_hand:
        return "computer"
    else:
        return "no winner"

def get_player_hand():
    while True:
        try:
            player_hand = int(input(f"Play a hand between {HAND_MIN} and {HAND_MAX}: "))
    
            if player_hand >= HAND_MIN and player_hand <= HAND_MAX:
                return player_hand
    
            print("Invalid Hand")
        except ValueError:
            print("Invalid Input")

def get_player_guess():
    while True:
        try:
            player_guess = int(input(f"Guess the sum of both hands between {HAND_MIN * 2} and {HAND_MAX * 2}: "))

            if player_guess >= HAND_MIN * 2 and player_guess <= HAND_MAX * 2:
                return player_guess

            print("Invalid Guess")
        except ValueError:
            print("Invalid Input")

def get_stats(player_score, player_wins, computer_score, computer_wins):
    return  f"============================\n" \
            f"\tPlayer Score:\t{player_score}\n" \
            f"\tPlayer Wins:\t{player_wins}\n" \
            f"\tComputer Score:\t{computer_score}\n"\
            f"\tComputer Wins:\t{computer_wins}\n"

def get_play_again_prompt():
    while True:
        response = input("Do you want to play again (yes or quit): ").lower()

        if response == "yes" or response == "quit":
            return response
        else:
            print("Invalid Response\n")

def main():
    # These variables are predefined for you. Do not remove them.
    player_score = 0
    player_wins = 0
    computer_score = 0
    computer_wins = 0
    game_round = 1

    # STUDENT CODE HERE
    # Implement the game workflow below.
    # Refer to the README.md for the game requirements.
    print(get_game_header())

    while True:
        if game_round > 1:
            print(get_stats(player_score, player_wins, computer_score, computer_wins))

        print(f"Game Round: {game_round}")

        computer_hand = get_computer_hand()
        computer_guess = get_computer_guess()
        # to cheat on the computer only!! LoL
        # print(f"Computer Hand: {computer_hand}")

        player_hand = get_player_hand()
        player_guess = get_player_guess()

        print(f"Player Hand: {player_hand} - Player Guess: {player_guess}")
        print(f"Computer Hand: {computer_hand} - Computer Guess: {computer_guess}")
        print(f"Combined Hand: {player_hand + computer_hand}")

        winner = determine_winner(player_hand, player_guess, computer_hand, computer_guess)

        print(f"Winner: {winner}")

        if winner == "tie":
            print("It's a Tie. No points awarded.")
        elif winner == "player":
            player_score += generate_xp(game_round)
            player_wins += 1
        elif winner == "computer":
            computer_score += generate_xp(game_round)
            computer_wins += 1
        else:
            print("No Winner")

        print()

        play_again = get_play_again_prompt()

        if play_again == "yes":
            game_round += 1

            continue

        if play_again == "quit":
            break

    # PREDEFINED BELOW, DO NOT MODIFY ANY CODE
    print("Thank you for playing Morra!")


# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was ended abruptly by the user\n")
    