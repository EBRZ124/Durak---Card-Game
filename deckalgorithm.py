import random
import numpy as np

# diamonds 0 -> 12
# hearts 13 - 25
# spades 26 -> 38
# clubs 39 -> 51
the_deck = ["♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦Jack", "♦Queen", "♦King", "♦Ace",
            "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥Jack", "♥Queen", "♥King", "♥Ace",
            "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠Jack", "♠Queen", "♠King", "♠Ace",
            "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣Jack", "♣Queen", "♣King", "♣Ace"]

trump = ["♦", "♥", "♠", "♣"]

player = []
player_attacks = ["", "", "", "", "", ""]
opponent = []
opponent_attacks = ["", "", "", "", "", ""]

def player_card():
    range = len(the_deck)
    card = random.randint(0, range - 1)

    opponent.append(the_deck[card])
    the_deck.pop(card)

def opponent_card():
    range = len(the_deck)
    card = random.randint(0, range - 1)

    player.append(the_deck[card])
    the_deck.pop(card)

for i in range (0, 6):
    player_card()
    opponent_card()

cards_left = len(the_deck)

trump_cards = random.randint(0, 3)

trump_type = trump[trump_cards]

#print(cards_left)
#print(f"Trump cards: {trump_type}")
#print(f"Your deck: {player}")
#print(f"Opponents deck: {opponent}")

def check_card():
    pass

def place_card():
    pass

