
import random


DECK_FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
DECK_SUITS = ['diamonds', 'clubs', 'hearts', 'spades' ]

VALUES  = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': [1, 11]
}


def generate_random_card():
    while True:
        face = random.choice(DECK_FACES)
        suit = random.choice(DECK_SUITS)
        value = VALUES[face]
        yield (face, value, suit)

card_generator = generate_random_card()