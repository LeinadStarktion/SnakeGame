#Importación de librería y ubicación del marcador en la pantalla

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#Características del marcador

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orange")#Color del marcador
        self.penup()
        self.goto(0, 270)#Rango minimo y máximo de puntuación posible
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}"
,

align=ALIGNMENT, font=FONT)
#Mensaje de alerta que indica que el jugador a perdido

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
align=ALIGNMENT, font=FONT) #Valor a mostrar en pantalla

#Propiedades para escalar el marcador

    def increase_score(self):
        self.score += 1

        self.clear()
        self.update_scoreboard()