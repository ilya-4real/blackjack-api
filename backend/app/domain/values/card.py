from dataclasses import dataclass, field
from typing import Literal, TypeAlias

from domain.values.base import BaseValueObject

DECK_FACES_TYPE: TypeAlias = Literal[
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "jack",
    "queen",
    "king",
    "ace",
]
DECK_SUITS_TYPE: TypeAlias = Literal["diamonds", "clubs", "hearts", "spades"]

FACE_VALUE_MAP: dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 11,
}


@dataclass(frozen=True)
class Card:
    face: DECK_FACES_TYPE
    suit: DECK_SUITS_TYPE

    @property
    def value(self) -> int:
        return FACE_VALUE_MAP[self.face]
