from dataclasses import dataclass

@dataclass
class Player:
    name: str
    game_score: int = 0


class TennisGame:
    
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2