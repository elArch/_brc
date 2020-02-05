import pytest
from src.Pen import Pen


def test_default_initial_pen():
    pen = Pen()
    assert pen.ink_container_value == 1000
    assert pen.size_letter == 1.0
    assert pen.color == 'blue'
