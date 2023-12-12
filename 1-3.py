from turtle import *
t = Turtle()
t.color("blue")
t.shape("turtle")
t.speed(10)
t.pensize(5)
def plus():
    left(90)
    forward(100)
    right(90)
    forward(50)
    left(90)
    backward(100)
    right(90)
for i in range(4):
    plus()
    right(90)