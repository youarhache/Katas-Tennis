from tennis import TennisGame, Player


def test_can_create_player():
    player = Player(name="Nadal")

    assert isinstance(player, Player)
    assert player.name == "Nadal"


def test_can_create_a_game():
    game = TennisGame()

    assert isinstance(game, TennisGame)
