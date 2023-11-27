import turtle

image="turtle1.gif"

turtle_screen = turtle.Screen()
turtle_screen.title("Catch the Turtle")

theTurtle=turtle.Turtle()


turtle_screen.addshape(image)
theTurtle.shape(image)
turtle.mainloop()