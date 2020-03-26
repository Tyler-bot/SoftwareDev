import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

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
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("orange")
food.penup()
food.goto(0,100)

segments = []

# Bonus food
bonus = turtle.Turtle()
bonus.speed(0)
bonus.shape("circle")
bonus.color("red")
bonus.penup()
bonus.goto(0,-100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" SNEK by Tyler ", align="center", font=("Fixedsys", 24, "normal"))

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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("SNEK by Tyler  High Score: {}".format(high_score), align="center", font=("Fixedsys", 24, "normal")) 


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
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Fixedsys", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("SNEK by Tyler  High Score: {}".format(high_score), align="center", font=("Fixedsys", 24, "normal"))


    # Bonus points
    if head.distance(bonus) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        bonus.goto(x,y)

        score += 25
        delay += 0.001

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Fixedsys", 24, "normal"))
    
        if score > high_score:
            high_score = score

    # Making sure the food's never stack over each other
    if bonus.distance(food) < 20:
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

    time.sleep(delay)

wn.mainloop()