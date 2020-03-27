import random 	
import time

# My take on an InspireBot where you get a random compliment/ 
# inspirational quote, hopefully keep developing this and eventually
# make it into an app.

inspiring = [
"Your limitation—it's only your imagination.",
"You've got this!", 
"Dream big kiddo!", 
"It's all gonna be worth it in the end!",
"You're doing so well!", 
"The harder you work for something the greater the reward when you get it!"
]

complimenting = [
"You're so pretty!", 
"Your eyes are like stars.",
"You're looking amazing!", 
"You look great!", 
"You look a million dollars!", 
"Nothing compares to you!", 
"Truly angelic!"
]

while True:

    print("Hi there!")
    print("What's your name?")
    myName = input()

    print("Who do you wish to inspire/compliment?")
    Name = input()

    print(Name + " is the name of the person, would you like to inspire or compliment them?")
    print("Please type either 'inspire' or 'compliment'.")

    Inspire = input()

    if Inspire == "inspire":

        print("Hi there " + Name + "!")
        time.sleep(1)
        print("This is a message from " + myName)
        time.sleep(1)
        print("As " + myName + " believes you could do with some inspiring from me!")
        time.sleep(3)
        print("How lazy of " + myName + "!")
        time.sleep(2)
        print("At least the thoughts there I suppose, and I'm not all that bad..")
        time.sleep(3)
        print("ANYWAYS I'm rambling! here's your inspiration " + Name + "!!")
        time.sleep(2)
        print(" ")
        print(" ")
        print(random.choice(inspiring))
        print(" ")
        print(" ")

        while True:
            print("Run again? (y/n): ")
            answer = input()
            if answer in ("y", "n"):
                break
            print("Invalid input.")
        if answer == "y":
            continue
        else:
            print("Goodbye")
            break

    else:

        Compliment = input()

        print("Hi there " + Name + "!")
        time.sleep(1)
        print("This is a message from " + myName)
        time.sleep(1)
        print("As " + myName + " believes you could do with some compliments from me!")
        time.sleep(3)
        print("How lazy of " + myName + "!")
        time.sleep(2)
        print("Lucky for you I'm amazing at giving compliments endlessly!")
        time.sleep(3)
        print("ANYWAYS enough about me, heres your compliment " + Name + "!!")
        time.sleep(2)
        print(" ")
        print(" ")
        print(random.choice(complimenting))
        print(" ")
        print(" ")

        while True:
            print("Run again? (y/n): ")
            answer = input()
            if answer in ("y", "n"):
                break
            print("Invalid input.")
        if answer == "y":
            continue
        else:
            print("Goodbye")
            break




