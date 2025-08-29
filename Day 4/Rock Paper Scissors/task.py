import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Wrong number, try again!")

print("Computer chose:")

game = [rock, paper, scissors]

length = len(game)

computer = random.randint(0,length - 1)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choice == computer:
    print("It's a draw!")
elif choice == 0 & computer == 1:
    print("You lose!")
elif choice == 0 & computer == 2:
    print("You win!")
elif choice == 1 & computer == 0:
    print("You win!")
elif choice == 1 & computer == 2:
    print("You lose!")
elif choice == 2 & computer == 0:
    print("You lose!")
elif choice == 2 & computer == 1:
    print("You win!")




