import turtle

from random import randint
image="turtle1.gif"




skorTablosu = turtle.Turtle()
skorTablosu.penup()
skorTablosu.hideturtle()
skorTablosu.setposition(-290, 310)


skor_metni = "Skor: 100"
skorTablosu.write(skor_metni, False, align='left', font=('Arial', 14, 'normal'))




turtle_screen = turtle.Screen()
turtle_screen.title("Catch the Turtle")

theTurtle=turtle.Turtle()
theTurtle.penup()

turtle_screen.addshape(image)
theTurtle.shape(image)
while 1==1:
    theTurtle.goto(randint(-300,300),randint(-300,300))










turtle.mainloop()