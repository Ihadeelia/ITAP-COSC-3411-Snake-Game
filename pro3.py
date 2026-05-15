#!/usr/bin/python
from turtle import *
import turtle
import random
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("#eaffd0")
screen.setup(800, 800)
screen.tracer(0)
screen.addshape("apple.gif")


player = Turtle()
player.shape("circle")
player.color("blue")
player.penup()
player.goto(0, 0)
player.direction = "stop"


player2 = Turtle()
player2.shape("circle")
player2.color("pink")
player2.penup()
player2.goto(-100, 0)
player2.direction = "right"

player2_segments = []

food = Turtle()
food.shape("apple.gif")
food.penup()
food.goto(100, 100)

segments = []

score = 0
high_score = 0

score2 = 0
high_score2 = 0

pen = Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write(f"Player 1 Score: {score}  Player 1 High Score: {high_score}",
          align="center", font=("Arial", 12, "bold"))


pen2 = Turtle()
pen2.speed(0)
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -350)
pen2.write(f"Player 2 Score: {score2} Player 2 High Score: {high_score2}",
           align="center", font=("Arial", 12, "bold"))

def go_up():
    if player.direction != "down":
        player.direction = "up"

def go_down():
    if player.direction != "up":
        player.direction = "down"

def go_left():
    if player.direction != "right":
        player.direction = "left"

def go_right():
    if player.direction != "left":
        player.direction = "right"

def move():
    if player.direction == "up":
        player.sety(player.ycor() + 10)
    if player.direction == "down":
        player.sety(player.ycor() - 10)
    if player.direction == "left":
        player.setx(player.xcor() - 10)
    if player.direction == "right":
        player.setx(player.xcor() + 10)

def move_player2():
    if player2.xcor() < food.xcor():
        player2.setx(player2.xcor() + 10)
    elif player2.xcor() > food.xcor():
        player2.setx(player2.xcor() - 10)

    if player2.ycor() < food.ycor():
        player2.sety(player2.ycor() + 10)
    elif player2.ycor() > food.ycor():
        player2.sety(player2.ycor() - 10)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")


while True:
    screen.update()

   
    if abs(player.xcor()) > 390 or abs(player.ycor()) > 390:

        time.sleep(1)
        player.goto(0, 0)
        player.direction = "stop"

        
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0

        
        score2 = 0

        
        pen.clear()
        pen.write(f"Player 1 Score : {score}  Player 1 High Score : {high_score}",
                  align="center", font=("Arial", 12, "bold"))

        pen2.clear()
        pen2.write(f"Player 2 Score : {score2}  Player 2 High Score : {high_score2}",
                   align="center", font=("Arial", 12, "bold"))

   
    if player.distance(food) < 20:
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        food.goto(x, y)

        new_segment = Turtle()
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Player 1 Score: {score}  Player 1 High Score : {high_score}",
                  align="center", font=("Arial", 12, "bold"))
    
    if player2.distance(food) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)

        new_player2_segment = Turtle()
        new_player2_segment.shape("circle")
        new_player2_segment.color("violet")
        new_player2_segment.penup()
        player2_segments.append(new_player2_segment)

        score2 += 10
        if score2 > high_score2:
            high_score2 = score2

        pen2.clear()
        pen2.write(f"Player 2 Score: {score2}  Player 2 High Score: {high_score2}",
                   align="center", font=("Arial", 12, "bold"))

    
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(player.xcor(), player.ycor())

 
    for index in range(len(player2_segments) - 1, 0, -1):
        x = player2_segments[index - 1].xcor()
        y = player2_segments[index - 1].ycor()
        player2_segments[index].goto(x, y)

    if len(player2_segments) > 0:
        player2_segments[0].goto(player2.xcor(), player2.ycor())

    move()
    move_player2()

    time.sleep(0.1)

screen.mainloop()
