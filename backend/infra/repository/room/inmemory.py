from uuid import UUID

from domain.entities.player import Player
from domain.entities.room import Room
from infra.repository.room.interface import RoomRepository


class InMemoryRoomRepository(RoomRepository):
    rooms: list[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_room(self, room_id: UUID) -> Room:
        return [room for room in self.rooms if room.oid == room_id][0]

    def add_player_to_room(self, player: Player, room_id: UUID) -> None:
        room = [room for room in self.rooms if room.oid == room_id][0]
        room.connect_player(player)

    def remove_player_from_room(self, player: Player, room_id: UUID) -> None:
        room = [room for room in self.rooms if room.oid == room_id][0]
        room.disconnect_player(player)
