from dataclasses import dataclass

@dataclass
class Player:
    name: str
    game_score: int = 0


class TennisGame:
    pass