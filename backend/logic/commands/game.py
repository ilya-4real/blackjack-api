from uuid import UUID
from domain.values.wager import Wager
from infra.repository.game.base import GameRepository
from logic.commands.base import BaseCommand, BaseCommandHandler
from dataclasses import dataclass


@dataclass
class PlaceWagerCommand(BaseCommand):
    game_id: UUID
    wager: Wager


@dataclass
class GetCardCommand(BaseCommand):
    game_id: UUID


@dataclass
class StandWithCurrentCardsCommand(BaseCommand):
    game_id: UUID


@dataclass
class PlaceWagerCommandHandler(BaseCommandHandler[PlaceWagerCommand, None]):
    game_repository: GameRepository

    def handle(self, command: PlaceWagerCommand) -> None:
        game = self.game_repository.get_game(command.game_id)
        game.place_wager(command.wager)
