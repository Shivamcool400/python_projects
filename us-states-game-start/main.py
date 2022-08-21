import turtle
import pandas

screen = turtle.Screen()
screen.title("Us state Games")
image = "blank_states_img.gif"
screen.addshape(image)
tim = turtle.Turtle()
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
allstate = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50,Guess the name", prompt="What is the name of another state").title()
    if answer_state == "Exit":
        missingstate = []
        for state in allstate:
            if state not in guessed_states:
                missingstate.append(state)
        new_data = pandas.DataFrame(missingstate)
        new_data.to_csv("statestolearn.csv")
        break
    if answer_state in allstate:
        guessed_states.append(answer_state)
        state = data[data.state == answer_state]
        x_cor = int(state.x)
        y_cor = int(state.y)
        print(x_cor)
        print(y_cor)
        tim.penup()
        tim.hideturtle()
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)


