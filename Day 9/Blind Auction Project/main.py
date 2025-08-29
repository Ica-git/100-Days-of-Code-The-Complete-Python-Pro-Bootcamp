# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

def find_winner(bids):
    max_bid = 0
    winner = ""

    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            winner = key

    print(f"The winner is {winner} with a bid of ${max_bid}")


print(logo)
print("Welcome to the secret auction program.")

to_continue = True
player_count = 0

bids = {}

while to_continue:

    if player_count > 0:
        print("\n" * 20)

    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    decision = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bids[name] = int(bid)

    player_count += 1

    if decision == "no":
        to_continue = False


find_winner(bids)