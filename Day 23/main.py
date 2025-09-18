from turtle import Turtle, Screen
from chick import Chick
from car import Car
import time
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Cross")

screen.tracer(0)

chick = Chick()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(chick.move, "Up")

cars = []
game_is_on = True

while game_is_on:

    if random.randint(1, 6) == 1:
        new_car = Car()
        cars.append(new_car)

    time.sleep(chick.game_speed)
    screen.update()

    for car in cars:
        car.car_move()

    for car in cars:
        if chick.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    if chick.ycor() > 280:
        scoreboard.level_up()
        chick.car_speed_up()
        chick.to_start()


screen.exitonclick()

