from dataclasses import dataclass
from uuid import UUID

from domain.entities.player import Player
from domain.entities.room import Room
from infra.repository.room.interface import RoomRepository
from logic.commands.base import BaseCommand, BaseCommandHandler


@dataclass
class CreateRoomCommand(BaseCommand):
    player: Player


@dataclass
class ConnectToRoomCommand(BaseCommand):
    room_id: UUID
    player: Player


@dataclass
class CreateRoomCommandHandler(BaseCommandHandler[CreateRoomCommand, Room]):
    room_repository: RoomRepository

    def handle(self, command: CreateRoomCommand) -> Room:
        room = Room()
        room.connect_player(command.player)
        self.room_repository.add_room(room)
        return room


@dataclass
class ConnectToRoomCommandHandler(
    BaseCommandHandler[ConnectToRoomCommand, None]
):
    room_repository: RoomRepository

    def handle(self, command: ConnectToRoomCommand) -> None:
        self.room_repository.add_player_to_room(
            command.player, command.room_id
        )
