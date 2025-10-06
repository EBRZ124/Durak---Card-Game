import random
import numpy as np

diamonds = ["♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦Jack", "♦Queen", "♦King", "♦Ace"]
hearts = ["♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥Jack", "♥Queen", "♥King", "♥Ace"]
spades = ["♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠Jack", "♠Queen", "♠King", "♠Ace"]
clubs = ["♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣Jack", "♣Queen", "♣King", "♣Ace"]

player = []
opponent = []

for i in range (0, 5):
    type = random.randint(0, 3)
    if type == 0:
        type = diamonds
    if type == 1:
        type = hearts
    if type == 2:
        type = spades
    if type == 3:
        type = clubs

    range = len(type)
    card = random.randint(0, range - 1)

    player.append(type[card])
    type.pop(card)

    range = len(type)
    card = random.randint(0, range - 1)

    opponent.append(type[card])
    type.pop(card)

print(f"Your deck: {player}")
print(f"Opponents deck: {opponent}")
