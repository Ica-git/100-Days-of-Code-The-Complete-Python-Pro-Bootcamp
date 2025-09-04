# import packages
from game_data import  data
from art import logo,vs
import random


def format_data(number):
    name = data[number]["name"]
    desc = data[number]["description"]
    country = data[number]["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(user_answer, a_followers, b_followers):
    if a_followers > b_followers:
        return user_answer == "a"
    else:
        return user_answer == "b"



#first print
print(logo)

length = len(data)
num2 = random.randint(0,length)

score = 0
keep_playing = True

while keep_playing:
    num1 = num2
    num2 = random.randint(0, length)

    while num1 == num2:
        num2 = random.randint(0, length)

    # print(f"Compare A: {data[num1]['name']}, "
    #             f"{data[num1]['description']}, {data[num1]['country']}")
    print(f"Compare A: {format_data(num1)}")

    print(vs)
    print(f"Against B: {format_data(num2)}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_followers_count = data[num1]["follower_count"]
    b_followers_count = data[num2]["follower_count"]

    is_correct = check_answer(answer, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        num1 = num2
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_playing = False


