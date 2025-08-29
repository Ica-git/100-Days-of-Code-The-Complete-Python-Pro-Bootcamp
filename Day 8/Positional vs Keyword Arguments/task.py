# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}")

greet_with(name = "Masa", location = "Pancevo")

def calculate_love_score(name1, name2):
    # Convert names to lowercase so counting works regardless of case
    combined_names = (name1 + name2).lower()

    # Count letters from "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    # Count letters from "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    # Combine into a two-digit number
    love_score = int(str(true_count) + str(love_count))

    print(love_score)
    return love_score


# Example test
calculate_love_score("Kanye West", "Kim Kardashian")

