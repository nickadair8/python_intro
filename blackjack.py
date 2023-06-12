import random

cards = []
suits = ["kings", "hearts", "diamonds", "clubs"]
ranks = ["A", "2", "3", "4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cardsDealt = []
    for x in range(number):
        cardsDealt.append(cards.pop())
    return cardsDealt

shuffle()

card = deal(1)[0]