from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0

    if 11 in deck and sum(deck) == 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)

def compare(score_user, score_computer):
    if score_user == score_computer:
        return "Draw!"
    elif score_computer == 0:
        return "You lose!"
    elif score_user == 0:
        return "You win!"
    elif score_user > 21:
        return "You lose!"
    elif score_computer > 21:
        return "You win!"
    elif score_user > score_computer:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            elif user_choice == 'n':
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == "y":
    print("\n" * 20)
    print(logo)
    play_game()

