from dataclasses import dataclass, field
from random import choice
from typing import get_args

from domain.entities.base import BaseEntity
from domain.values.card import DECK_FACES_TYPE, DECK_SUITS_TYPE, Card

DECK_FACES = get_args(DECK_FACES_TYPE)
DECK_SUITS = get_args(DECK_SUITS_TYPE)


@dataclass
class Dealer(BaseEntity):
    cards: list[Card] = field(default_factory=list)

    @staticmethod
    def pull_a_card() -> Card:
        return Card(choice(DECK_FACES), choice(DECK_SUITS))

    def decide_next_step(self) -> None:
        if self.cards_sum < 17:
            self.cards.append(self.pull_a_card())

    @property
    def cards_sum(self) -> int:
        return sum([card.value for card in self.cards])
