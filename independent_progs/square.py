import turtle


screen = turtle.Screen()
screen.bgcolor("black")

t= turtle.Turtle()
t.speed(0)
t.pensize(8)
t.showturtle()


colors = ["red","orange","green","yellow","blue","purple"]


for i in range(2222):
	t.color(colors[i%6])
	t.forward(i*2)
	t.left(145)

screen.exitonclick()
