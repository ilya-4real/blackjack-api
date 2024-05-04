from uuid import UUID

from domain.entities.game import Game
from infra.repository.game.base import GameRepository


class InMemoryGameRepository(GameRepository):
    games: list[Game] = []

    def add_game(self, game: Game):
        self.games.append(game)

    def get_game(self, game_id: UUID) -> Game:
        return [game for game in self.games if game.oid == game_id][0]

    def update_game(self, game: Game): ...
