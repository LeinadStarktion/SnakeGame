#Importación de la librería 
from turtle import Turtle
import random

#Definición de la clase de Food para establecer las caracteristicas del objeto que comera la culebra en cuestión

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle") #Forma del círculo
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)

#Propiedades que adquirira la culebra al comer consecuentemente uno de comida

        self.color("white")#Color de la baya
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)#Reestablece la posición de la próxima baya
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)