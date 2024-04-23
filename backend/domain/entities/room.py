from dataclasses import dataclass, field
from enum import Enum

from domain.entities.base import BaseEntity
from domain.entities.game import Game
from domain.entities.player import Player
from domain.events.room import RoomGameFinishedEvent, RoomGameStartedEvent
from domain.exceptions.room import GameAlreadyStartedError, NoStartedGameError


class RoomStatus(Enum):
    IN_GAME = 1
    WAITING = 2


@dataclass
class Room(BaseEntity):
    status: RoomStatus = field(default=RoomStatus.WAITING)
    players: set[Player] = field(default_factory=set)
    game: Game = field(init=False)

    def start_new_game(self):
        if self.status == RoomStatus.IN_GAME:
            raise GameAlreadyStartedError(
                "can not start a new game while current is going on"
            )
        self.game = Game(self.players)
        self.register_event(RoomGameStartedEvent(self.oid))

    def finish_game(self):
        if self.status == RoomStatus.WAITING:
            raise NoStartedGameError("there is no active game to finish")
        self.register_event(RoomGameFinishedEvent(self.oid))

    def connect_player(self, player: Player):
        self.players.add(player)

    def disconnect_player(self, player: Player):
        self.players.remove(player)
