from turtle import Screen, Turtle
from data import question_data

my_screen = Screen()
my_screen.setup(800, 600)
my_screen.bgcolor("white")
my_screen.title("Are You Smarter Than Chris?")


style = ('Courier', 20, 'bold')

score = 0
chris_score = 0
question_number = 0
chris_race_x = -350
user_race_x = -350


def main():
    my_screen.listen()
    start_turtle = intro()
    start_turtle.onclick(clicked_start_button)
    my_screen.mainloop()


def create_button(x, y, file):
    name = Turtle()
    my_screen.addshape(file)
    name.shape(file)
    name.penup()
    name.goto(x, y)

    return name


def create_text_x_y(text, color, font, x, y):
    text_turtle = Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(x, y)
    text_turtle.pencolor(color)
    text_turtle.write(text, font=font)


def create_text_align(text, color, font, x, y):
    text_turtle = Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(x, y)
    text_turtle.pencolor(color)
    text_turtle.write(text, font=font, align="center")


def intro():
    my_screen.tracer(0)
    create_text_align("Are You Smarter Than Chris?", color="black", font=('Courier', 20, 'normal'), x=0, y=250)
    create_text_align("Here is a computer science quiz for you and Chris!", color="black",
                      font=('Courier', 20, 'normal'), x=0, y=210)
    create_text_align("Let's see who can answer more questions.", color="black", font=('Courier', 20, 'normal'),
                      x=0, y=170)
    start_button = create_button(x=-10, y=20, file="start_button.gif")
    my_screen.update()
    return start_button


def split_q_two_line(split_q):
    first_line_list = split_q[0:7]
    second_line_list = split_q[7:]
    first_line = " ".join(first_line_list)
    second_line = " ".join(second_line_list)

    return first_line, second_line


def new_question():
    global question_number, question_data
    next_question = question_data[question_number]["question"]
    split_question = next_question.split()

    if len(split_question) > 7:
        first_line, second_line = split_q_two_line(split_question)
        create_text_align(f"Q.{question_number + 1}: {first_line}", color="black", font=('Courier', 20, 'bold'), x=0,
                          y=250)
        create_text_align(f"{second_line}", color="black", font=('Courier', 20, 'bold'), x=0,
                          y=210)
    else:
        create_text_align(f"Q.{question_number+1}: {next_question}", color="black", font=('Courier', 20, 'bold'),
                          x=0, y=250)


def user_input_setup():
    global yes_button, no_button
    yes_button = create_button(x=-140, y=110, file="true.gif")
    yes_button.custom_attribute = "True"
    yes_button.onclick(clicked_yes_button)

    no_button = create_button(x=140, y=110, file="false.gif")
    no_button.custom_attribute = "False"
    no_button.onclick(clicked_no_button)
    return yes_button, no_button


def race_setup():
    global score, question_number, question_data, chris_score
    chris_racer = create_button(x=chris_race_x, y=-200, file="chris.gif")
    user_racer = create_button(x=user_race_x, y=-140, file="user.gif")
    create_text_x_y(text=f"Your score: {score}/{len(question_data)}", color="black", font=('Courier', 12, 'normal'),
                    x=-370, y=-258)
    create_text_x_y(text=f"Chris's score: {chris_score}/{len(question_data)}", color="black",
                    font=('Courier', 12, 'normal'), x=-370, y=-280)
    race_track()
    return chris_racer, user_racer


def race_track():
    x = -370
    y = -109
    for i in range(3):
        drawer = Turtle()
        drawer.hideturtle()
        drawer.penup()
        drawer.goto(x, y)
        drawer.pendown()
        drawer.pensize(3)
        drawer.goto(x+700, y)
        y -= 61

    #vertical line
    drawer.penup()
    drawer.goto(333, -108)
    drawer.pendown()
    drawer.goto(333, -232)
    #finish line text&start line text
    create_text_x_y(text="Finish line", color="black", font=('Courier', 16, 'bold'), x=265, y=-100)
    create_text_x_y(text="Start", color="black", font=('Courier', 16, 'bold'), x=-372, y=-100)


def clicked_start_button(x, y):
    my_screen.clear()
    my_screen.tracer(0)
    global question_number
    global question_data
    new_question()
    yes_button, no_button = user_input_setup()
    race_setup()
    my_screen.update()
    return yes_button, no_button


def still_has_questions():
    global question_number
    global question_data
    if question_number < len(question_data):
        return True
    else:

        return False


def clicked_yes_button(x, y):

    my_screen.clear()
    my_screen.tracer(0)
    check_answer(yes_button)
    if still_has_questions():
        next_button = create_button(x=-10, y=20, file="next.gif")
        race_setup()
        my_screen.update()
        next_button.onclick(full_loop)
        return next_button
    else:
        my_screen.clear()
        final_score()


def clicked_no_button(x, y):
    my_screen.clear()
    my_screen.tracer(0)
    check_answer(no_button)
    if still_has_questions():
        next_button = create_button(x=-10, y=20, file="next.gif")
        race_setup()
        my_screen.update()
        next_button.onclick(full_loop)
        return next_button
    else:
        my_screen.clear()
        final_score()


def check_answer(clicked_button):
    global score, user_race_x, chris_race_x, question_number, chris_score
    correct_answer = question_data[question_number]["correct_answer"]
    if clicked_button.custom_attribute == correct_answer:
        score += 1
        chris_score += 1
        user_race_x += 33
        chris_race_x += 33

        create_text_align("You are right.", color="black", font=('Courier', 20, 'normal'), x=0, y=250)
        create_text_align("But Chris was right too.", color="black",
                          font=('Courier', 20, 'normal'), x=0, y=210)
    else:
        chris_race_x += 33
        chris_score += 1
        create_text_align("That was wrong.", color="black", font=('Courier', 20, 'normal'), x=0, y=250)
        create_text_align(text="But Chris was right.", color="black",
                          font=('Courier', 20, 'normal'), x=0, y=210)
        create_text_align(f"The correct answer is: {correct_answer}.", color="black", font=('Courier', 20, 'normal'),
                          x=0, y=170)
    question_number += 1


def final_score():
    global score, question_number, question_data
    if score < len(question_data):
        create_text_align(f"Your final score is: {score}", color="blue", font=('Courier', 20, 'bold'), x=0, y=250)
        create_text_align(text=f"Chris's final score is: {len(question_data)}", color="blue",
                          font=('Courier', 20, 'bold'), x=0, y=210)
        create_text_align("Chris won! Maybe next time...", color="blue", font=('Courier', 20, 'bold'),
                          x=0, y=170)
        my_screen.tracer(0)
        race_setup()
        my_screen.update()
    else:
        create_text_align(f"Your final score is: {score}", color="blue", font=('Courier', 20, 'bold'), x=0, y=250)
        create_text_align(text=f"Chris's final score is: {len(question_data)}", color="blue",
                          font=('Courier', 20, 'bold'), x=0, y=210)
        create_text_align("Congratulations! It is a tie.", color="blue", font=('Courier', 20, 'bold'),
                          x=0, y=170)
        my_screen.tracer(0)
        race_setup()
        my_screen.update()


def full_loop(x, y):
    my_screen.clear()
    my_screen.tracer(0)
    new_question()
    user_input_setup()
    race_setup()
    my_screen.update()


if __name__ == "__main__":
    main()
