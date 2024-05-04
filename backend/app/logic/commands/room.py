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
class LeaveRoomCommand(BaseCommand):
    room_id: UUID
    player: Player


@dataclass
class StartNewGameCommand(BaseCommand):
    room_id: UUID


@dataclass
class CreateRoomCommandHandler(BaseCommandHandler[CreateRoomCommand, Room]):
    room_repository: RoomRepository

    def handle(self, command: CreateRoomCommand) -> Room:
        room = Room(command.player)
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


@dataclass
class LeaveRoomCommandHandler(BaseCommandHandler[LeaveRoomCommand, None]):
    room_repository: RoomRepository

    def handle(self, command: LeaveRoomCommand) -> None:
        self.room_repository.remove_player_from_room(
            command.player, command.room_id
        )


@dataclass
class StartNewGameCommandHandler(
    BaseCommandHandler[StartNewGameCommand, UUID]
):
    room_repository: RoomRepository

    def handle(self, command: StartNewGameCommand) -> UUID:
        room = self.room_repository.get_room(command.room_id)
        room.start_new_game()
        return room.game.oid
