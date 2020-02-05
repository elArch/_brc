import pytest
import random
import string
from src.Pen import Pen


@pytest.fixture()
def random_ink():
    return random.randint(0, 10000)


@pytest.fixture()
def random_size():
    return round(random.uniform(0.0, 100.0), 2)


@pytest.fixture()
def random_average_word():
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=random.randint(0, 1000)))


@pytest.fixture()
def random_longest_word():
    return ''.join(random.choices(string.ascii_uppercase +
                                  string.digits, k=random.randint(1001, 2001)))

@pytest.fixture()
def my_default_pen():
    return Pen()

@pytest.fixture()
def my_positive_custom_pen():
    positive_pen = Pen(
        ink_container_value=10000,
        size_letter=10.0,
        color='pink'
    )
    return positive_pen

@pytest.fixture()
def my_negative_ink_pen():
    my_negative_ink_pen = Pen(
        ink_container_value=-1000,
        size_letter=1.0,
        color='pink'
    )
    return my_negative_ink_pen

@pytest.fixture()
def my_negative_font_size_pen():
    negative_font_size_pen = Pen(
        ink_container_value=1000,
        size_letter=-1.0,
        color='pink'
    )
    return negative_font_size_pen





@pytest.mark.parametrize(




#@pytest.mark.parametrize(
#    'ink_container_value,'
#    'font_size,'
#    'color',
#    [
#        (-1000, 1.00, 'pink'),
#        (1000, -1.00, 'pink'),
#        (-1000, -1.0, 'pink')
#    ]
#)