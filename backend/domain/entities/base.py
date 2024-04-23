from abc import ABC
from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from domain.events.base import BaseEvent


@dataclass
class BaseEntity(ABC):
    oid: UUID = field(default_factory=uuid4, kw_only=True)
    _events: list[BaseEvent] = field(default_factory=list, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)

    def register_event(self, event: BaseEvent):
        self._events.append(event)

    def pull_events(self):
        events = copy(self._events)
        self._events.clear()
        return events

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: "BaseEntity") -> bool:
        return self.oid == __value.oid
