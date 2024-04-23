from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from logic.mediator.eventmediator import EventMediator


@dataclass
class BaseCommand(ABC): ...


CommandType = TypeVar("CommandType", bound=BaseCommand)
CommandResult = TypeVar("CommandResult")


@dataclass
class BaseCommandHandler(ABC, Generic[CommandType, CommandResult]):
    _mediator: EventMediator

    @abstractmethod
    def handle(self, command: CommandType) -> CommandResult: ...
