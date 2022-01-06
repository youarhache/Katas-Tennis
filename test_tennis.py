import pytest
from tennis import TennisGame, Player, GamePlayers


@pytest.fixture
def nadal():
    return Player("Nadal")


@pytest.fixture
def federer():
    return Player("Federer")


@pytest.fixture
def new_game(nadal, federer):
    return TennisGame(nadal, federer)


def test_can_create_player():
    player = Player(name="Nadal")

    assert isinstance(player, Player)
    assert player.name == "Nadal"


def test_can_create_a_game(federer, nadal):
    game =TennisGame(nadal, federer)

    assert isinstance(game, TennisGame)
    assert game.player1 == nadal
    assert game.player2 == federer


def test_can_add_point_to_player(new_game, federer, nadal):
    new_game.add_point(player=GamePlayers.player1)

    assert new_game.player1.game_score == 1
    assert new_game.player2.game_score == 0
    
