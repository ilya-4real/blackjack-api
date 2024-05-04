from dataclasses import dataclass

from domain.exceptions.application import ApplicationException


@dataclass
class GameAlreadyStartedError(ApplicationException):
    msg: str


@dataclass
class NoStartedGameError(ApplicationException):
    msg: str
