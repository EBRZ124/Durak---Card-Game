import random

diamonds = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
hearts = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
spades = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
clubs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

player = []
opponent = []

for i in range (0, 5):
    type = random.randint(0, 3)
    card = random.randint(0, 12)
    if type == 0:
        player.append(diamonds[card])
    if type == 1:
        player.append(hearts[card])
    if type == 2:
        player.append(spades[card])
    if type == 3:
        player.append(clubs[card])


for i in range (0, 5):
    type = random.randint(0, 3)
    card = random.randint(0, 12)
    if type == 0:
        opponent.append(diamonds[card])
    if type == 1:
        opponent.append(hearts[card])
    if type == 2:
        opponent.append(spades[card])
    if type == 3:
        opponent.append(clubs[card])

print(f"Your deck: {player}")
print(f"Opponents deck: {opponent}")