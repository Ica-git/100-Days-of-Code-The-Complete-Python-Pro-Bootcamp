import turtle as t
import random

screen = t.Screen()
screen.setup(500,400)

def move(turtle):
    movement = random.randint(0,10)
    turtle.forward(movement)




colors = ["red","blue","green","yellow","orange","purple"]

x_cordinate = -230
y_cordinate = -100

all_turtles = []

for i in range(6):
    temp_turtle = t.Turtle("turtle")
    temp_turtle.penup()
    temp_turtle.color(colors[i])
    temp_turtle.teleport(x_cordinate, y_cordinate)
    y_cordinate = y_cordinate + 40
    all_turtles.append(temp_turtle)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        move(turtle)
        if(turtle.xcor() > 230):
            is_race_on = False
            if(turtle.color()[1] == user_bet):
                print("Congratulations, you won!")
            else:
                print(f"You lost, {turtle.color()[1]} won!")















screen.exitonclick()
