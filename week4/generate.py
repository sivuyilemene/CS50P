import numbers
import random
# get a random item from list of chosen items
coin = random.choice(["heads", "tails"])
print(coin)

# get a random int from numbers a <= N <= b
number = random.randint(1,10)
print(number)

# shuffle list  
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)