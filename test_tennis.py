from tennis import TennisGame


def test_can_create_a_game():
    game = TennisGame()

    assert isinstance(game, TennisGame)
