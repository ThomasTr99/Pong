#Simple pong in Python 3

import turtle
import pygame

wn = turtle.Screen()
wn.title("Pong+ by Thomas Tran")
wn.bgcolor('black')
wn.setup(width=1000, height=800)
wn.tracer(0)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Donkey-Kong-Country-Simian-Segue-_Restored_.wav")
pygame.mixer.music.play()


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-380,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(380,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .30
ball.dy = .30


#Scoring
score_a = 0
score_b = 0

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,360)
pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Paddle_a Up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#Paddle_a Down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#Paddle_b Up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#Paddle_b Down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#Keyboard bindings for Paddle_a
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

#Keyboard bindings for Paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wn.update()
    

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border checking
    if ball.ycor() > 390:
        ball.sety(390)
        #reverses the direction
        ball.dy *= -1
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1

    if ball.xcor() > 495:
        #Sets the ball in the middle when it hits the side walls
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        '''ball.dx = .25
        ball.dy = .25'''
    if ball.xcor() < -495:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        '''ball.dx = .25
        ball.dy = .25'''

    #Paddle and Ball Collision
    if ball.xcor() < -370 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1
        '''ball.dx *= 1.03
        ball.dy *= 1.03'''
    if ball.xcor() > 370 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        '''ball.dx *= 1.03
        ball.dy *= 1.03'''
    