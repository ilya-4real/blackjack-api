from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar


@dataclass
class BaseEvent(ABC): ...


EventType = TypeVar("EventType", bound=BaseEvent)
EventResult = TypeVar("EventResult")


@dataclass
class BaseEventHandler(ABC, Generic[EventType, EventResult]):
    @abstractmethod
    def handle(self, command: EventType) -> EventResult: ...
