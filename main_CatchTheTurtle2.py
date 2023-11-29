import turtle
import random
screen=turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch The Turtle")
FONT = ('Arial',25,'normal')
score=0
game_over=False
#turtle_list

turtle_list=[]
score_turtle = turtle.Turtle()

#countdown_turtle

countdown_turtle = turtle.Turtle()



#score turtle
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("darkblue")
    top_height=screen.window_height()/2
    y=top_height * 0.7
    score_turtle.penup()
    score_turtle.goto(0,y)
    score_turtle.write(arg="Score : ", move=False, align="center", font=(FONT))


grid_size=10
def make_turtle(x,y):
    t= turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score : {score}", move=False, align="center", font=(FONT))
        #print(x,y)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("darkgreen")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)
#make turtle properties
x_Coordinates=[-20,-10,0,10,20]
y_Coordinates=[20,10,0,-10]

def setup_turtles():
    for x in x_Coordinates:
        for y in y_Coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_turtles()
    hide_turtles()
    setup_score_turtle()
    show_turtles_randomly()
    countdown(20)
    turtle.tracer(1)



start_game_up()








turtle.mainloop()
