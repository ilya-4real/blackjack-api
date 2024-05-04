from dataclasses import dataclass
from uuid import UUID

from domain.events.base import BaseEvent


@dataclass(frozen=True)
class RoomGameStartedEvent(BaseEvent):
    room_id: UUID

    @property
    def message(self):
        return f'in room number "{self.room_id}" started a new game'


@dataclass(frozen=True)
class RoomGameFinishedEvent(BaseEvent):
    room_id: UUID

    @property
    def message(self):
        return f'in room number "{self.room_id}" finished a game'
