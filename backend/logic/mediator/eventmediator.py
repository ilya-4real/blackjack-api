from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.events.base import BaseEvent


@dataclass
class EventMediator(ABC):
    @abstractmethod
    def register_event(self, event: type[BaseEvent]) -> None:
        raise NotImplementedError

    @abstractmethod
    def publish_events(self, events: list[BaseEvent]):
        raise NotImplementedError
