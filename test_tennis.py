from tennis import TennisGame, Player


def test_can_create_player():
    player = Player(name="Nadal")

    assert isinstance(player, Player)
    assert player.name == "Nadal"


def test_can_create_a_game():
    player1 = Player("Nadal")
    player2 = Player("Federer")

    game = TennisGame(player1, player2)

    assert isinstance(game, TennisGame)
    assert game.player1 == player1
    assert game.player2 == player2
