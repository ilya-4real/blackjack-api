from dataclasses import dataclass

from domain.exceptions.bank import NegativeBankException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Bank(BaseValueObject[int]):
    def validate(self):
        if self.value < 0:
            raise NegativeBankException("negative bank")
