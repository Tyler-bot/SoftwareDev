import turtle
import os
import math
import random
import winsound

delay = 0.1
# Register the shapes

turtle.register_shape("invader.gif")
turtle.register_shape("ship2.gif")

# Screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by Tyler")
wn.bgpic("background.gif")
wn.tracer(2)

# Intro music

winsound.PlaySound("intro_music", winsound.SND_ASYNC)



# Draw border

penb = turtle.Turtle()
penb.speed(0)
penb.color("white")
penb.penup()
penb.setpos(-300, -300)
penb.pendown()
penb.pensize(3)
for side in range(4):
    penb.forward(600)
    penb.left(90)

penb.hideturtle()

# Set the score

score = 0

# Draw the score

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setpos(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Fixedsys", 14, "normal"))
score_pen.hideturtle()
# Player Turtle

player = turtle.Turtle()
player.color("yellow")
player.shape("ship2.gif")
player.shapesize(0.5, 0.5)
player.penup()
player.speed(0)
player.setpos(0, -250)
player.setheading(90)

playerspeed = 15


# Multiple Enemies
number_of_enemies = 5
number_of_enemies2 = 5
# Create an empty list of enemies 
enemies = []


# Add enemies to the the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.shapesize(0.5, 0.5)
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setpos(x, y)

    

enemyspeed = 1

# Weapon

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Bullet states: 
# Ready and Fire

bulletstate = "ready"

# Functions

# A - D movement functions

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x <-280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

# Weapon function

def fire_bullet():
    # Declare bulletsate as global if it needs changes
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("gun", winsound.SND_ASYNC)
        bulletstate = "fire"
        # Move the bullet above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setpos(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else: 
        return False


# Key bindings

turtle.listen()

turtle.onkey(move_left, "A")
turtle.onkey(move_left, "a")
turtle.onkey(move_left, "Left")


turtle.onkey(move_right, "D")
turtle.onkey(move_right, "d")
turtle.onkey(move_right, "Right")

turtle.onkey(fire_bullet, "space") 


# Main game loop

while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemies direction
            enemyspeed *= -1


        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemies direction
            enemyspeed *= -1
        
        if enemy.xcor() > 0 and enemy.ycor() < -260:
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)


        # Boundary Check
        if enemy.xcor() < -20 and enemy.ycor() < -280:
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)

    
        

        #Check for collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("zap", winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setpos(0,-400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)
            #Update the score
            score += 10
            scorestring = "Score %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Fixedsys", 14, "normal"))

        if isCollision(player, enemy):
            winsound.PlaySound("death", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER!")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
    




delay = input("Press enter to finish.")
