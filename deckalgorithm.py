import random
import numpy as np

diamonds = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
hearts = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
spades = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
clubs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

player = []
opponent = []

for i in range (0, 5):
    type = random.randint(0, 3)
    if type == 0:
        range = len(diamonds)
        card = random.randint(0, range - 1)

        player.append(diamonds[card])
        diamonds.pop(card)

        range = len(diamonds)
        card = random.randint(0, range - 1)

        opponent.append(diamonds[card])
        diamonds.pop(card)

    if type == 1:
        range = len(hearts)
        card = random.randint(0, range - 1)

        player.append(hearts[card])
        hearts.pop(card)

        range = len(hearts)
        card = random.randint(0, range - 1)

        opponent.append(hearts[card])
        hearts.pop(card)

    if type == 2:
        range = len(spades)
        card = random.randint(0, range - 1)

        player.append(spades[card])
        spades.pop(card)

        range = len(spades)
        card = random.randint(0, range - 1)

        opponent.append(spades[card])
        spades.pop(card)

    if type == 3:
        range = len(clubs)
        card = random.randint(0, range - 1)

        player.append(clubs[card])
        clubs.pop(card)

        range = len(clubs)
        card = random.randint(0, range - 1)

        opponent.append(clubs[card])
        clubs.pop(card)


print(f"Your deck: {player}")
print(f"Opponents deck: {opponent}")
