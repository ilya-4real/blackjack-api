from dataclasses import dataclass

from domain.exceptions.application import ApplicationException


@dataclass
class StackIsFullException(ApplicationException):
    msg: str

    @property
    def message(self):
        return f"players stack is full {self.msg}"


@dataclass
class NegativeWagerException(ApplicationException):
    msg: str

    @property
    def message(self):
        return f"wager can not be negative {self.msg}"
