#Importación libreria y posiciones iniciales de la serpiente

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,
0)]
MOVE_DISTANCE = 20 #Distancia que recorre la misma
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Atribuír propiedades de creación y segmentación de la culebra
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
                self.add_segment(position)
    #Características de la serpiente, además de su posición 

    def add_segment(self, position):
        new_segment = Turtle("square")#Forma de la serpiente
        new_segment.color("yellow")#Color
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)#Agrega un segmento adicional a medida que esta crece

    def extend(self):

        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):
#Definición de los segementos de campo basados en las coordenadas de X & Y respectivamente

            new_x = self.segments[seg_num -1].xcor()

            new_y = self.segments[seg_num -1].ycor()

            self.segments[seg_num].goto(new_x,new_y)

#Epilogo de la funcionalidad en cuanto al movimiento y la distancia en base a las instrucciones del jugador

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)