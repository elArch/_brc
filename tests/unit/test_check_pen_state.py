from src.Pen import Pen

# Default ink_value = 1000
# Empty ink_value = 0
# Prohibited ink_value = -1000

prohibited_ink_value_kwargs_1 = {
    'ink_container_value': -1000,
    'size_letter': 1.0,
    'color': 'red'
}
empty_ink_value_kwargs = {
    'ink_container_value': 0,
    'size_letter': 1.0,
    'color': 'red'
}

default_kwargs_3 = {
    'ink_container_value': 1000,
    'size_letter': 1.0,
    'color': 'red'
}

ink_values = [-1000, 0, 1000]


def test_default_check_pen_state():
    pen = Pen()
    assert pen.check_pen_state() is True
