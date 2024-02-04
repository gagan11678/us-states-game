import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('US States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states_df = pandas.read_csv('50_states.csv')
states = states_df.state.to_list()
screen.tracer(0)

state_list = []

tim = Turtle()
tim.hideturtle()
tim.penup()
no_of_guess = 0

while len(state_list) < 50:
    screen.update()
    user_input = screen.textinput(f'You Guessed: {no_of_guess}/50', 'Enter a State Name').title()

    if user_input == 'Exit':
        missing_states = [state for state in states if state not in state_list]
        missing_ans = pandas.DataFrame(missing_states)
        missing_ans.to_csv('missing_ans.csv', index=False)
        break
    elif user_input in states:
        state_list.append(user_input)
        no_of_guess += 1
        cor = states_df[states_df.state == user_input]
        tim.goto(int(cor.x), int(cor.y))
        tim.write(user_input)


