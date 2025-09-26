#TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
bids = {}

game_is_on = True
print(art.logo)
print("Welcome to the secret auction program.")

while game_is_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    to_continue = input("Are there any other bidders? 'yes' or 'no': ").lower()
    if to_continue == "no":
        game_is_on = False
    else:
        print("\n"*20)

winner_name = ""
max_bet = 0
for key in bids:
    if bids[key] > max_bet:
        winner_name = key
        max_bet = bids[key]

print(f"{winner_name} is the winning bidder, with the bid of {max_bet}.")