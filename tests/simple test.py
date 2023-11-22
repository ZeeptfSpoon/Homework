import pytest
from binarysearcgamepc import binary_search_game
def test_first():
    assert binary_search_game(10)

def test_negative():
    with pytest.raises(TypeError):
        binary_search_game("-1")
