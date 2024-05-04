from dataclasses import dataclass

from domain.exceptions.application import ApplicationException


@dataclass
class TooLongNameException(ApplicationException):
    msg: str

    @property
    def message(self):
        return f"player cannot have name longer than 50 chars, {self.msg}"
