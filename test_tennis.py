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


def test_can_add_point_to_player(new_game):
    new_game.add_point(player=GamePlayers.player1)

    assert new_game.player1.game_score == 1
    assert new_game.player2.game_score == 0
    
def test_score_return_love_when_zero(new_game):
    current_score = new_game.score()

    assert current_score == "Nadal: Love - Federer: Love"


def test_score_when_player2_has_one_then_fifteen(new_game):
    new_game.player2.game_score = 1

    current_score = new_game.score()

    assert current_score == "Nadal: Love - Federer: Fifteen"


def test_score_when_player1_has_one_then_fifteen(new_game):
    new_game.player1.game_score = 1

    current_score = new_game.score()

    assert current_score == "Nadal: Fifteen - Federer: Love"


def test_score_when_player1_has_2_then_thirty(new_game):
    new_game.player1.game_score = 2

    current_score = new_game.score()

    assert current_score == "Nadal: Thirty - Federer: Love"


def test_score_when_player2_has_2_then_thirty(new_game):
    new_game.player2.game_score = 2

    current_score = new_game.score()

    assert current_score == "Nadal: Love - Federer: Thirty"


def test_score_when_player1_has_3_then_forty(new_game):
    new_game.player1.game_score = 3

    current_score = new_game.score()

    assert current_score == "Nadal: Forty - Federer: Love"


def test_score_when_player2_has_3_then_forty(new_game):
    new_game.player2.game_score = 3

    current_score = new_game.score()

    assert current_score == "Nadal: Love - Federer: Forty"


def test_score_when_both_player_at_3_then_deuce(new_game):
    new_game.player1.game_score = 3
    new_game.player2.game_score = 3

    current_score = new_game.score()

    assert current_score == "Deuce"


def test_score_when_both_player_above_3_and_equal_then_deuce(new_game):
    new_game.player1.game_score = 5
    new_game.player2.game_score = 5

    current_score = new_game.score()

    assert current_score == "Deuce"


def test_score_when_both_player_above_3_and_player1_winnig_then_advantage(new_game):
    new_game.player1.game_score = 5
    new_game.player2.game_score = 4

    current_score = new_game.score()

    assert current_score == "Nadal: Advantage - Federer: _"


def test_score_when_both_player_above_3_and_player2_winnig_then_advantage(new_game):
    new_game.player1.game_score = 3
    new_game.player2.game_score = 4

    current_score = new_game.score()

    assert current_score == "Nadal: _ - Federer: Advantage"


def test_get_winner_when_still_no_winner_then_none(new_game):
    winner = new_game.get_winner()

    assert winner is None


def test_gat_winner_when_player1_win_then_player1(new_game):
    new_game.player1.game_score = 4

    winner = new_game.get_winner()

    assert winner == new_game.player1