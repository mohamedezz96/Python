from turtle import Turtle

class Snake:
    def __init__(self):
        self.__snake = []
        x = 0
        for i in range(3):
            snake_part= Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(x,0)
            x += 20
            self.__snake.append(snake_part)

    def move(self):
        for i in range(len(self.__snake)-1, 0, -1):
            next_x = self.__snake[i-1].xcor()
            next_y = self.__snake[i-1].ycor()
            self.__snake[i].goto(next_x,next_y)
        
        self.__snake[0].forward(20)

    def up(self):
        if self.__snake[0].heading() != 270:
            self.__snake[0].setheading(90)
            

    def Down(self):
        if self.__snake[0].heading() != 90:
            self.__snake[0].setheading(270)

    def Right(self):
        if self.__snake[0].heading() != 180:
            self.__snake[0].setheading(0)

    def Left(self):
        if self.__snake[0].heading() != 0:
            self.__snake[0].setheading(180)

    def head(self):
        return self.__snake[0]
    
    def increase_snake(self):
        new_part= Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.__snake[-1].position())
        self.__snake.append(new_part)

    def detect_collision(self):
        
        for i in range(1,len(self.__snake)-1):
            distance = self.__snake[0].distance(self.__snake[i])
            if distance < 10:
                return True
        
        return False
