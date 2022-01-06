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
    
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2

    def add_point(self, player: GamePlayers) -> None:
        if player == GamePlayers.player1:
            self.player1.game_score += 1
        elif player == GamePlayers.player2:
            self.player2.game_score += 1

    def score(self):
        return f"{self.player1.name}: Love - {self.player2.name}: {self.get_score_name(self.player2.game_score)}"

    @staticmethod
    def get_score_name(score):
        if score == 0:
            return "Love"
        return "Fifteen"