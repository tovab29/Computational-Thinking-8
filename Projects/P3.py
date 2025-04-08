# Beggining 

import turtle 

t = turtle.Turtle ()

#Middle
turtle.Screen ().bgcolor ("black")
colors = ["pink","cyan","red"]
for i in range ( 70 ):
    t.color( colors[ i % 3 ] )
    t.forward( 8 )
    t.left( 45 )
t.color("cyan")
for i in range(700):
    t.forward(100)
    t.left(72)

turtle.exitonclick()


