from turtle import Turtle, Screen
t = Turtle()
s = Screen()
s.listen()


def forwards():
    t.forward(10)


def backwards():
    t.backward(10)


def counter_clock():
    t.left(10)


def clock():
    t.right(10)


def clears():
    t.clear()
    t.penup()
    t.setpos(0,0)
    t.pendown()



s.onkey(key="d", fun=forwards)
s.onkey(key="a", fun=backwards)
s.onkey(key="w", fun=clock)
s.onkey(key="s", fun=counter_clock)
s.onkey(key="c", fun=clears)

s.exitonclick()
