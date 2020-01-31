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
