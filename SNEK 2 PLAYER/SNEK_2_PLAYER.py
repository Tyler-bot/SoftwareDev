import turtle
import time
import random

delay = 0.1

# Score
player_one = 0
player_two = 0

# Set up the screen
wn = turtle.Screen()
wn.title("SNEK by tyler")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(60) # Turns off the screen updates


# Border turtle graphic
mypen = turtle.Turtle()
mypen.penup()
mypen.setpos(-290,-290)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(580)
    mypen.left(90)
mypen.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(-100,0)
head.direction = "stop"

# Snake head 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("green")
head2.penup()
head2.goto(100,0)
head2.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("purple")
food.penup()
food.goto(0,100)

segments = []
segments2 = []

# Bonus food
bonus = turtle.Turtle()
bonus.speed(0)
bonus.shape("circle")
bonus.color("red")
bonus.penup()
bonus.goto(0,-100)

# Obstacles
#obs = turtle.Turtle()
#obs.speed(0)
#obs.shape("square")
#obs.shapesize(1,2)
#obs.color("black")
#obs.penup()
#obs.goto(0,0)



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" SNEK 2 PLAYER by Tyler ", align="center", font=("Fixedsys", 24, "normal"))


pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
#pen2.write(" PRESS WASD OR IJKL TO PLAY! ", align= "center", font=("Fixedsys", 15,"normal"))
pen2.pendown()

if head.xcor()>-100 or head.ycor()> 0:
    pen2.clear()
    pen2.write("test")

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up2():
    if head2.direction != "down":
        head2.direction = "up"

def go_down2():
    if head2.direction != "up":
        head2.direction = "down"

def go_left2():
    if head2.direction != "right":
        head2.direction = "left"

def go_right2():
    if head2.direction != "left":
        head2.direction = "right"

def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)

    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_up, "W")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_down, "S")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "D")


wn.listen()
wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")



# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0)
        head.goto(-100,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        player_one = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal")) 

    if head2.xcor()>290 or head2.xcor()<-290 or head2.ycor()>290 or head2.ycor()<-290:
        time.sleep(0)
        head2.goto(100,0)
        head2.direction = "stop"

        # Hide the segments
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        
        # Clear the segments list
        segments2.clear()

        # Reset the score
        player_two = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal")) 

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light yellow")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.002

        # Increase the score
        player_one += 10
        
    
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal")) 


    if head2.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        # Add a segment
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color("light green")
        new_segment2.penup()
        segments2.append(new_segment2)

        # Shorten the delay
        delay -= 0.002

        # Increase the score
        player_two += 10

        
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal")) 

    # Bonus points
    if head.distance(bonus) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        bonus.goto(x,y)

        player_one += 25

        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))
    
    if head2.distance(bonus) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        bonus.goto(x,y)

        player_two += 25

        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))


    # Making the obstacle hit-reg

    #if head.distance(obs) < 20:
        #time.sleep(0)
        #head.goto(100,0)
        #head.direction = "stop"

        # Hide the segments
        #for segment in segments:
            #segment.goto(1000, 1000)
        
        # Clear the segments list
        #segments.clear()

        # Reset the score
        #player_one = 0

        # Reset the delay
        #delay = 0.1

        #pen.clear()
        #pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))

    #if head2.distance(obs) < 20:
        #time.sleep(0)
        #head2.goto(-100,0)
        #head2.direction = "stop"

        # Hide the segments
        #for segment2 in segments2:
            #segment2.goto(1000, 1000)
        
        # Clear the segments list
        #segments2.clear()

        # Reset the score
        #player_two = 0

        # Reset the delay
        #delay = 0.1

        #pen.clear()
        #pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))


    # Making sure the food's never stack over each other
    if bonus.distance(food) < 20:
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x,y)


    move() 
    move2()   

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head2) < 20:
            time.sleep(1)
            head2.goto(-100,0)
            head2.direction = "stop"
        
            # Hide the segments
            for segment in segments2:
                segment2.goto(1000, 1000)
        
            # Clear the segments list
            segments2.clear()

            # Reset the score
            player_two = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))

    for segment2 in segments2:
        if segment2.distance(head) < 20:
            time.sleep(1)
            head.goto(100,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            player_two = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))

            # Check if collision between snakes

    for segment in segments:
        if segment.distance(head2) < 20:
            time.sleep(1)
            head.goto(-100,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            player_one = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))


    for segment2 in segments2:
        if segment2.distance(head) < 20:
            time.sleep(1)
            head2.goto(100,0)
            head2.direction = "stop"
        
            # Hide the segments
            for segment2 in segments2:
                segment2.goto(1000, 1000)
        
            # Clear the segments list
            segments2.clear()

            # Reset the score
            player_two = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(player_one, player_two), align="center", font=("Fixedsys", 24, "normal"))

    
            

    time.sleep(delay)

wn.mainloop()