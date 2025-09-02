
from art import logo
import random

PLAYER_LIVES = 0

def check_answer(user_guess, actual_answer, PLAYER_LIVES):
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess < number:
        print("Your guess is too low.")
        return PLAYER_LIVES - 1
    else:
        print("Your guess is too high.")
        return PLAYER_LIVES - 1


def difficulty_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    else:
        return  5



print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


number = random.randint(1, 100)


PLAYER_LIVES = difficulty_level()

while PLAYER_LIVES > 0:
    print(f"You have {PLAYER_LIVES} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    PLAYER_LIVES = check_answer(guess, number, PLAYER_LIVES)

    if PLAYER_LIVES == 0:
         print("You've run out of guesses. You lose.")

# while PLAYER_LIVES > 0:
#     print(f"You have {PLAYER_LIVES} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if guess == number:
#         print(f"You got it! The answer was {number}.")
#         break
#     elif guess < number:
#         PLAYER_LIVES -= 1
#         print("Your guess is too low.")
#     else:
#         PLAYER_LIVES -= 1
#         print("Your guess is too high.")
#
#     if PLAYER_LIVES == 0:
#         print("You've run out of guesses.")



