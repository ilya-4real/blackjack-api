from dataclasses import dataclass

from domain.entities.player import Player
from logic.events.base import BaseEvent, BaseEventHandler


@dataclass
class PlayerSwitchedEvent(BaseEvent):
    switched_to_player: Player


@dataclass
class PlayerSwitchedEventHandler(BaseEventHandler[PlayerSwitchedEvent, str]):
    def handle(self, event: PlayerSwitchedEvent) -> str:
        return f"player switched to {event.switched_to_player.name}"
