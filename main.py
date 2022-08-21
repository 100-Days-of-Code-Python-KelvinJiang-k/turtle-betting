from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    return r, g, b


is_race_on = False
num_turtles = 6
turtles = []

valid_bet = False
while not valid_bet:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a number: ")
    if type(user_bet) is None or not user_bet.isnumeric() or not 0 < int(user_bet) <= num_turtles:
        print("Invalid input. Please try again.")
    else:
        valid_bet = True
user_bet = int(user_bet) - 1

for turtle_index in range(num_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(random_color())
    turtle_gap = 400 / (num_turtles + 1)
    new_turtle.goto(x=-230, y=((turtle_gap - 200) + (turtle_gap * turtle_index)))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_index in range(len(turtles)):
        rand_distance = random.randint(0, 10)
        turtles[turtle_index].forward(rand_distance)

        if turtles[turtle_index].xcor() > 230:
            is_race_on = False
            if user_bet == turtle_index:
                print(f"You have won the bet. The winning turtle is #{user_bet + 1}!")
            else:
                print(f"You have lost the bet. The winning turtle is #{user_bet + 1}.")

screen.exitonclick()
