rank = "K"
value = 10
suits = ["kings", "hearts", "diamonds", "clubs"]
suit = suits[1]
print("Your card is: " + rank + " of " + suit)
suits.append("snakes")
for suit in suits:
    print(suit)
