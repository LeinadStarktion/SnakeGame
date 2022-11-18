#Importación de librerías pertinentes para dar inicio a la creación del juego en cuestión

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Detalles y características que tendra la pantalla

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Definición de actores y objetos base

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Modalidad de controles del jugador 

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

    #Detectar la comida a partir de las colisiones de la culebra con la misma 

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detectar colisión de la culebra con el muro

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detección de colisión de la culebra con su propia cola

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

############################################################################################################################################################

screen.exitonclick()