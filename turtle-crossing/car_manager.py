from turtle import  Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.dist = STARTING_MOVE_DISTANCE

    def createcar(self):
        random_chance = random .randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.shapesize(stretch_len=2)
            car.setheading(180)
            car.goto(380, random.randint(-250, 250))
            self.cars.append(car)




    def move(self):
        for cars in self.cars:
         cars.forward(self.dist)


    def levelup(self):
        self.dist += MOVE_INCREMENT



