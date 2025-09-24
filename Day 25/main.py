import pandas

#data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].median())
# print(data["temp"].max())

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.value_counts("Primary Fur Color"))
#
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray","Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

import turtle

df = pandas.read_csv("50_states.csv")

state_list = df.state.tolist()
print(state_list)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

game_is_on = True
guessed_states = []

while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(title=f"Guess the state!", prompt="What's another state name?").title()
    else:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct Guesses!", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        x_cor = int(df[df.state == answer_state].x.item())
        y_cor = int(df[df.state == answer_state].y.item())
        tom = turtle.Turtle()
        tom.teleport(x_cor, y_cor)
        tom.hideturtle()
        tom.write(f"{answer_state}", align="center", font=("Arial", 7, "bold"))
    elif answer_state is None:
        game_is_on = False


to_learn = []
for state in state_list:
    if state not in guessed_states:
        to_learn.append(state)

df = pandas.DataFrame(to_learn)
df.to_csv("to_learn.csv")








