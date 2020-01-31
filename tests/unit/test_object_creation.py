from src.Pen import Pen


def test_default_member_access():
    pen = Pen()
    assert pen.ink_container_value == 1000
    assert pen.size_letter == 1.0
    assert pen.color == 'blue'


def test_custom_object():
    pen = Pen(
        ink_container_value=10000,
        size_letter=100.0,
        color='red'
    )
    assert pen.ink_container_value == 10000
    assert pen.size_letter == 100.0
    assert pen.color == 'red'
