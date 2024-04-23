from dataclasses import dataclass
from typing import Literal

from domain.entities.base import BaseEntity
from domain.values.bank import Bank
from domain.values.playername import PlayerName


@dataclass(eq=False)
class Player(BaseEntity):
    name: PlayerName
    bank: Bank

    def deposit(self, amount: int) -> None:
        old_bank = self.bank.value
        self.bank = Bank(old_bank + amount)

    def write_off(self, amount: int):
        old_bank = self.bank.value
        self.bank = Bank(old_bank - amount)
