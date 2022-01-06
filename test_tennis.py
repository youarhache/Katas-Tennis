from tennis import TennisGame


def test_can_create_a_game():
    game = TennisGame(player1="Nadal", player2="Federer")

    assert isinstance(game, TennisGame)
    assert game.player1 == "Nadal"
    assert game.player2 == "Federer"
