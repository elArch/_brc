from src.Pen import Pen


def test_default_members_access():
    pen = Pen()
    assert pen.ink_container_value == 1000
    assert pen.size_letter == 1.0
    assert pen.color == 'blue'


def test_setting_initial_members():
    pen = Pen(
        ink_container_value=10,
        size_letter=100.0,
        color='pink'
    )
    assert pen.ink_container_value == 10
    assert pen.size_letter == 100.0
    assert pen.color == 'red'
