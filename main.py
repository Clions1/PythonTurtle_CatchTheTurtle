import turtle

from random import randint
image="turtle1.gif"

turtle_screen = turtle.Screen()
turtle_screen.title("Catch the Turtle")

theTurtle=turtle.Turtle()
theTurtle.penup()

turtle_screen.addshape(image)
theTurtle.shape(image)
while 1==1:
    theTurtle.goto(randint(-300,0),randint(0,400))








turtle.mainloop()