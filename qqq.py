import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("lol")
wn.setup(1000,750)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Line():
    def __init__(self,x,y,color,thickness):
        self.x = x
        self.y = y
        self.color = color
        self.length = 600
        self.heading = 270
        self.thickness = thickness

    def render_line(self,pen):
        pen.goto(self.x,self.y)
        pen.setheading(self.heading)
        pen.color(self.color)
        pen.pendown()
        pen.width(self.thickness)
        pen.fd(self.length)


class Border():
    def __init__(self,width,height,thickness):
        self.width = width
        self.height = height
        self.thickness = thickness

    def render_border(self, pen):
        pen.color("white")
        pen.width(self.thickness)
        pen.penup()

        left = -self.width/2
        right = self.width/2
        top = self.height/2
        bottom = -self.height/2


        pen.goto(left,top)
        pen.pendown()
        pen.goto(right,top)
        pen.goto(right,top/3)
        pen.penup()
        pen.goto(right,bottom/3)
        pen.pendown()
        pen.goto(right,bottom)
        pen.goto(left,bottom)
        pen.goto(left,bottom/3)
        pen.penup()
        pen.goto(left,top/3)
        pen.pendown()
        pen.goto(left,top)
        pen.penup()


class Player():
    def __init__(self, x, y, shape, color, shapesize):
        self.x = x 
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.da = 0
        self.thrust = 0
        self.acceleration = 0.1
        self.shapesize = shapesize
        self.width = 60
        self.height = 60

    def update(self):
        self.heading += self.da

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust

        self.x += self.dx
        self.y += self.dy

        self.border_check()

        player1.line_check1()
        player2.line_check2()

    def border_check(self):
        if self.x > border.width/2 - 30:
            self.x = border.width/2 - 30
            self.dx *= -1
        elif self.x < -border.width/2 + 30:
            self.x = -border.width/2 + 30
            self.dx *= -1
        if self.y > border.height/2 - 30:
            self.y = border.height/2 - 30
            self.dy *= -1
        elif self.y < -border.height/2 + 30:
            self.y = -border.height/2 + 30
            self.dy *= -1

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(self.shapesize)
        pen.stamp()

    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False
    

class Player1(Player):
    def __init__(self, x, y, shape, color,shapesize):
        Player.__init__(self,x,y,shape,color,shapesize)
        self.heading = 0

    def rotate_left1(self):
        self.da = 2
    
    def rotate_right1(self):
        self.da = -2
        
    def stop_rotation1(self):
        self.da = 0
    
    def accelerate1(self):
        self.thrust += self.acceleration
        if self.thrust > 0.025:
            self.thrust = 0.025
    
    def decelerate1(self):
        self.thrust = 0
    
    def line_check1(self):
        if self.x > line.x-45:
            self.x = line.x-45
            self.dx *= -1

    def reset_player1(self):
        self.x = -400
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.heading = 0


class Player2(Player):
    def __init__(self, x, y, shape, color,shapesize):
        Player.__init__(self,x,y,shape,color,shapesize)
        self.heading = 180

    def rotate_left2(self):
        self.da = 2

    def rotate_right2(self):
        self.da = -2
    
    def stop_rotation2(self):
        self.da = 0

    def accelerate2(self):
        self.thrust += self.acceleration
        if self.thrust > 0.025:
            self.thrust = 0.025
            
    def decelerate2(self):
        self.thrust = 0

    def line_check2(self):
        if self.x < line.x+45:
            self.x = line.x+45
            self.dx *= -1
        
    def reset_player2(self):
        self.x = 400
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.heading = 180



class Ball():
    def __init__(self, x, y, shape, color,shapesize):
        self.x = x 
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = shape
        self.color = color
        self.shapesize = shapesize
        self.width = 50
        self.height = 50
        self.heading = 0

    
    def update(self):

        self.x += self.dx
        self.y += self.dy

        self.ball_border_check()

    def ball_goal1(self):
        if -100<self.y<100 and self.x>500:
            return True
        else:
            return False
        
    def ball_goal2(self):
        if -100<self.y<100 and self.x<-500:
            return True
        else:
            return False

    
    def reset_ball(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0


    def ball_border_check(self):
        if self.y > border.height/2 - 30:
            self.y = border.height/2 - 30
            self.dy *= -1
        elif self.y < -border.height/2 + 30:
            self.y = -border.height/2 + 30
            self.dy *= -1
        if self.x > border.width/2 - 30 and self.y>100:
            self.x = border.width/2 - 30
            self.dx *= -1
        elif self.x < -border.width/2 + 30 and self.y<-100:
            self.x = -border.width/2 + 30
            self.dx *= -1
        if self.x > border.width/2 - 30 and self.y<-100:
            self.x = border.width/2 - 30
            self.dx *= -1
        elif self.x < -border.width/2 + 30 and self.y>100:
            self.x = -border.width/2 + 30
            self.dx *= -1


    def ball_render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(self.shapesize)
        pen.stamp()

class ScorePen1():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.score = 0
        self.scorestring = "%s" % self.score
    
    def update(self,pen):
        self.score += 1
        pen.clear()
        self.scorestring = "%s"%self.score

    def render_score_pen1(self,pen):
        pen.goto(self.x,self.y)
        pen.color(self.color)
        pen.write(self.scorestring,font = ("Arial",30))

class mh():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.mh = ":"
        
    def render_mh(self,pen):
        pen.goto(self.x,self.y)
        pen.color(self.color)
        pen.write(self.mh,font = ("Arial",40))


class ScorePen2():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.score = 0
        self.scorestring = "%s" % self.score

    def update(self,pen):
        self.score += 1
        pen.clear()
        self.scorestring = "%s"%self.score

    def render_score_pen2(self,pen):
        pen.goto(self.x,self.y)
        pen.color(self.color)
        pen.write(self.scorestring,font = ("Arial",30))

line = Line(0,300,"white",1)

border = Border(900,600,5)

player1 = Player1(-400,0,"turtle","red",3)

player2 = Player2(400,0,"turtle","blue",3)

ball = Ball(0,0,"circle","yellow",2.5)

scorepen1 = ScorePen1(-50,300,"red")
scorepen2 = ScorePen2(50,300,"blue")
mh = mh(0,300,"white")

players = []

players.append(player1)
players.append(player2)


wn.listen()

wn.onkeypress(player2.rotate_left2, "Left")
wn.onkeypress(player2.rotate_right2, "Right")
wn.onkeyrelease(player2.stop_rotation2, "Left")
wn.onkeyrelease(player2.stop_rotation2, "Right")
wn.onkeypress(player2.accelerate2, "Up")
wn.onkeyrelease(player2.decelerate2, "Up")

wn.onkeypress(player1.rotate_left1, "a")
wn.onkeypress(player1.rotate_right1, "d")
wn.onkeyrelease(player1.stop_rotation1, "a")
wn.onkeyrelease(player1.stop_rotation1, "d")
wn.onkeypress(player1.accelerate1, "w")
wn.onkeyrelease(player1.decelerate1, "w")

while True:
    pen.clear()

    for p in players:
        p.update()
    

    for p in players:
        p.render(pen)

    ball.update()

    for player in players:
        if player.is_collision(ball):
            ball.heading = player.heading
            ball.dx = player.dx
            ball.dy = player.dy
            ball.x += ball.dx
            ball.y += ball.dy
    
    if ball.ball_goal1():
        ball.reset_ball()
        player1.reset_player1()
        player2.reset_player2()
        scorepen1.update(pen)
    
    if ball.ball_goal2():
        ball.reset_ball()
        player1.reset_player1()
        player2.reset_player2()
        scorepen2.update(pen)

            
    line.render_line(pen)

    border.render_border(pen)

    ball.ball_render(pen)

    scorepen1.render_score_pen1(pen)
    scorepen2.render_score_pen2(pen)
    mh.render_mh(pen)


    wn.update()

