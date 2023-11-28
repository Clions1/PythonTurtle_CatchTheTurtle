import turtle

from random import randint
image="turtle1.gif"

score = 0


scoreTable = turtle.Turtle()
scoreTable.penup()
scoreTable.hideturtle()
scoreTable.setposition(-290, 310)


score_text = f"Score : {score}"
scoreTable.write(score_text, False, align='left', font=('Arial', 14, 'normal'))




turtle_screen = turtle.Screen()
turtle_screen.title("Catch the Turtle")

theTurtle=turtle.Turtle()
theTurtle.penup()

turtle_screen.addshape(image)
theTurtle.shape(image)
while 1==1:
    theTurtle.goto(randint(-300,300),randint(-300,300))










turtle.mainloop()