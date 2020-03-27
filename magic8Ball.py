import random
import time

print("Please type your question, and await a reply...")
question = input()

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
		return "It is decidely so"
	elif answerNumber == 3:
		return "Yes"
	elif answerNumber == 4:
		return "Reply hazy try again"
	elif answerNumber == 5:
		return "Most definitely!"
	elif answerNumber == 6:
		return "Is that even a real question?"
	elif answerNumber == 7:
		return "How about no"
	elif answerNumber == 8:
		return "The answer ain't so pretty"
	elif answerNumber == 9:
		return "Very doubtful"

r = random.randint(1,9)
fortune = getAnswer(r)
print("The answer to your question: " + question + " is...")
time.sleep(1)
print("...")
time.sleep(1)
print(fortune) 
