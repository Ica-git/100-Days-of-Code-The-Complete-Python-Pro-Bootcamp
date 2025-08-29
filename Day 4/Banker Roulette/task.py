import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

length = len(friends)

number = random.randint(0,length - 1)

# print(random.choice(friends))

name = friends[number]

print(f"{name} it's your turn to pay!")

