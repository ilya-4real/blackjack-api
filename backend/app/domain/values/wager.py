from dataclasses import dataclass

from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Wager(BaseValueObject[int]):
    def validate(self) -> None:
        if self.value < 0:
            raise
