from dataclasses import dataclass
from enum import Enum


MIN_POINTS_TO_WIN_GAME = 4
POINTS_DIFF_TO_WIN_GAME = 2
MIN_POINTS_TO_DEUCE = 3


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

    def score(self) -> str:
        if self.is_deuce():
            return "Deuce"
        elif self.is_advantage_palyer1():
            return f"{self.player1.name}: Advantage - {self.player2.name}: _"
        elif self.is_advantage_player2():
            return f"{self.player1.name}: _ - {self.player2.name}: Advantage"

        player1_score_name = self._score_names.get(self.player1.game_score)
        player2_score_name = self._score_names.get(self.player2.game_score)
        return f"{self.player1.name}: {player1_score_name} - {self.player2.name}: {player2_score_name}"

    def is_deuce(self) -> bool:
        return self.player1.game_score == self.player2.game_score >= MIN_POINTS_TO_DEUCE

    def is_advantage_player2(self) -> bool:
        return self.player2.game_score > self.player1.game_score >= MIN_POINTS_TO_DEUCE

    def is_advantage_palyer1(self) -> bool:
        return self.player1.game_score > self.player2.game_score >= MIN_POINTS_TO_DEUCE

    def get_winner(self) -> Player:
        if (self.player1.game_score >= MIN_POINTS_TO_WIN_GAME 
            and (self.player1.game_score - self.player2.game_score) >= POINTS_DIFF_TO_WIN_GAME):
            return self.player1
        elif (self.player2.game_score >= MIN_POINTS_TO_WIN_GAME 
            and (self.player2.game_score - self.player1.game_score) >= POINTS_DIFF_TO_WIN_GAME):
            return self.player2
        return None
