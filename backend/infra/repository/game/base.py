from uuid import UUID
from domain.entities.game import Game
from abc import ABC, abstractmethod


class GameRepository(ABC):
    @abstractmethod
    def add_game(self, game: Game):
        raise NotImplementedError

    @abstractmethod
    def get_game(self, game_id: UUID) -> Game:
        raise NotImplementedError

    @abstractmethod
    def update_game(self, game: Game):
        raise NotImplementedError
