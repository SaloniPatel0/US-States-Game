import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_input = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt="What's another state's name?").capitalize()
    print(answer_input)

    if answer_input == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_input in all_states:
        guessed_states.append(answer_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_input)

