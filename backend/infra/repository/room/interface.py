from abc import ABC, abstractmethod
from uuid import UUID

from domain.entities.player import Player
from domain.entities.room import Room


class RoomRepository(ABC):
    @abstractmethod
    def get_room(self, room_id: UUID) -> Room:
        raise NotImplementedError

    @abstractmethod
    def add_room(self, room: Room) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_player_to_room(self, player: Player, room_id: UUID) -> None:
        raise NotImplementedError
