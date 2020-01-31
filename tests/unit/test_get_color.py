from src.Pen import Pen

# Default ink color is blue
# Lets Try create Pen object with custom ink color for example used red color:
custom_kwargs = {
    'ink_container_value': 1000,
    'size_letter': 1.0,
    'color': 'red'
}


def test_default_ink_color_get_color():
    pen = Pen()
    assert pen.get_color() == pen.color


def test_custom_ink_color_get_color():
    pen = Pen(**custom_kwargs)
    assert pen.get_color() == pen.color
