from dataclasses import dataclass

from domain.exceptions.application import ApplicationException


@dataclass
class NegativeBankException(ApplicationException):
    msg: str

    @property
    def message(self):
        return f"negative bank account of player. {self.msg}"
