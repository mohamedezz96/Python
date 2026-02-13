from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.__food = Turtle("circle")
        self.__food.shapesize(0.5,0.5)
        self.__food.penup()
        self.__food.color("white")
        self.__food.goto(random.randint(-280,280),random.randint(-280,280))
    
    def food(self):
        return self.__food
    
    def change_food_position(self):
        self.__food.goto(random.randint(-280,280),random.randint(-280,280))
