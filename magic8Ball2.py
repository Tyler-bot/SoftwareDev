import random
messages = [
	"It is certain.",
	"Yes definitely!",
	"Is that even a real question?",
	"I'll have to think about that.",
	"Maybe yes, maybe no, but maybe yes.",
	"Sorry friend, it's a no.",
	"No.",
	"0% chance"
]

print(messages[random.randint(0, len(messages)-1)])
