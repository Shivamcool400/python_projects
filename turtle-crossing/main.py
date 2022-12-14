import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score= Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.createcar()
    car.move()
  #detect colloison
    for cars in car.cars:
        if cars.distance(player) < 20 :
            game_is_on = False
            score.gameover()
        if player.issuccesful():
            player.start()
            car.levelup()
            score.update()



    screen.update()

screen.exitonclick()