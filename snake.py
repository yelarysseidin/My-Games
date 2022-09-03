import turtle
import random
import time


delay = 0.1

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.shapesize(0.8)
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-230,230)
y = random.randint(-230,230)
food.goto(x,y)

segments = []

score = 0

highscore = 0

score_pen1 = turtle.Turtle()
score_pen1.speed(0)
score_pen1.color("white")
score_pen1.penup()
score_pen1.goto(-230,225)
scorestring1 = "Score: %s" %score
score_pen1.write(scorestring1,align = "left", font=("Arial",14))
score_pen1.hideturtle()

score_pen2 = turtle.Turtle()
score_pen2.speed(0)
score_pen2.color("white")
score_pen2.penup()
score_pen2.goto(225,225)
scorestring2 = "High Score: %s" %highscore
score_pen2.write(scorestring2,align = "right", font=("Arial",14))
score_pen2.hideturtle()


def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goright():
    if head.direction != "left":
        head.direction = "right"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    snakespeed = 20
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+snakespeed)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-snakespeed)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+snakespeed)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-snakespeed)


wn.listen()
wn.onkeypress(goup,"Up")
wn.onkeypress(godown,"Down")
wn.onkeypress(goright,"Right")
wn.onkeypress(goleft,"Left")


colors = ["green","blue","orange","purple","pink","yellow"]


while True:
    wn.update()
        
    if head.distance(food) < 20:
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        food.goto(x,y)

        score += 10

        
        if score>highscore:
            highscore = score

        scorestring1 = "Score: %s" %score
        scorestring2 = "High Score: %s" %highscore
        score_pen1.clear()
        score_pen2.clear()
        score_pen1.write(scorestring1,align = "left", font=("Arial",14))
        score_pen2.write(scorestring2,align = "right", font=("Arial",14))

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.shapesize(0.8)
        color = random.choice(colors)
        new_segment.color(color)
        new_segment.penup()

        segments.append(new_segment)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()


        score = 0

        scorestring1 = "Score: %s" %score
        score_pen1.clear()
        score_pen1.write(scorestring1,align = "left", font=("Arial",14))
    
    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear() 

                
            score = 0

            scorestring1 = "Score: %s" %score
            score_pen1.clear()
            score_pen1.write(scorestring1,align = "left", font=("Arial",14))


    time.sleep(delay)
wn.mainloop()
