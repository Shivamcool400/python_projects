import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for i in range (0,360,5):
  tim.color(random_color())
  tim.setheading(i)
  tim.circle(100)


screen  = t.Screen()
screen.exitonclick()
