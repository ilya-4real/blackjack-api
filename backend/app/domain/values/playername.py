from dataclasses import dataclass

from domain.exceptions.player import TooLongNameException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class PlayerName(BaseValueObject[str]):
    def validate(self):
        if len(self.value) > 50:
            raise TooLongNameException(self.value)
