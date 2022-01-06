from dataclasses import dataclass
from enum import Enum


@dataclass
class Player:
    name: str
    game_score: int = 0


class GamePlayers(Enum):
    player1 = 1
    player2 = 2


class TennisGame:
    _score_names = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }
    
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2

    def add_point(self, player: GamePlayers) -> None:
        if player == GamePlayers.player1:
            self.player1.game_score += 1
        elif player == GamePlayers.player2:
            self.player2.game_score += 1

    def score(self):
        if self.is_deuce():
            return "Deuce"
        elif self.is_advantage_palyer1():
            return f"{self.player1.name}: Advantage - {self.player2.name}: _"
        elif self.is_advantage_player2():
            return f"{self.player1.name}: _ - {self.player2.name}: Advantage"

        player1_score_name = self._score_names.get(self.player1.game_score)
        player2_score_name = self._score_names.get(self.player2.game_score)
        return f"{self.player1.name}: {player1_score_name} - {self.player2.name}: {player2_score_name}"

    def is_deuce(self):
        return self.player1.game_score == self.player2.game_score >= 3

    def is_advantage_player2(self):
        return self.player2.game_score > self.player1.game_score >= 3

    def is_advantage_palyer1(self):
        return self.player1.game_score > self.player2.game_score >= 3

    def get_winner(self):
        if self.player1.game_score == 4:
            return self.player1
        return None
