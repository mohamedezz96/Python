import colorgram
import random 
from turtle import Turtle, Screen, colormode

colormode(255)

colors = colorgram.extract("image.jpg", 300)
extracted_colors = []

for color in colors:
    extracted_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

t = Turtle()

t.speed(0) 
t.penup()

for j in range(0,501,50):
    t.goto(0, j)
    for i in range(10):
        t.dot(20, extracted_colors[random.randint(0,len(extracted_colors)-1)])  
        if i < 9:
            t.forward(50)
    

my_screen = Screen()
Screen().exitonclick()
