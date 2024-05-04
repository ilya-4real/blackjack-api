from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Generator

from domain.entities.base import BaseEntity
from domain.entities.dealer import Dealer
from domain.entities.player import Player
from domain.values.card import Card
from domain.values.wager import Wager


class GameResult(Enum):
    LOST = 1
    DRAW = 2
    WON = 3


@dataclass
class Game(BaseEntity):
    players: set[Player]
    current_player: Player = field(init=False)
    dealer: Dealer = field(default_factory=Dealer)
    player_generator: Generator[Player, None, None] = field(init=False)
    players_wagers_map: dict[Player, Wager] = field(init=False)
    players_cards_map: dict[Player, list[Card]] = field(init=False)

    def __post_init__(self):
        for player in self.players:
            self.players_wagers_map[player] = Wager(0)
            self.players_cards_map[player] = []

    def give_players_cards(self):
        for player in self.players_cards_map.keys():
            self.players_cards_map[player] = [
                self.dealer.pull_a_card() for i in range(2)
            ]

    def start_game(self):
        self.give_players_cards()
        self.player_generator = self.get_next_user()
        self.current_player = next(self.player_generator)

    def place_wager(self, wager: Wager) -> None:
        player = self.current_player
        player.write_off(wager.value)
        self.players_wagers_map[player] = wager

    def move_to_next_player(self):
        try:
            self.current_player = next(self.player_generator)
        except StopIteration:
            self.get_game_result()
        return self.current_player

    def get_card_for_player(self) -> tuple[Player, Card]:
        card = self.dealer.pull_a_card()
        self.players_cards_map[self.current_player].append(card)
        return self.current_player, card

    def get_next_user(self) -> Generator[Player, Any, None]:
        for player in self.players_cards_map.keys():
            yield player

    def get_game_result(self):
        result = {}
        for player, cards in self.players_cards_map.items():
            result[player] = self.get_result_for_player(
                cards, self.dealer.cards
            )
        return result

    @staticmethod
    def get_result_for_player(
        players_cards: list[Card], dealiers_cards
    ) -> GameResult:
        players_sum = sum([card.value for card in players_cards])
        dealers_sum = sum([card.value for card in dealiers_cards])
        if players_sum > dealers_sum:
            return GameResult.WON
        elif players_cards == dealiers_cards:
            return GameResult.DRAW
        else:
            return GameResult.LOST
