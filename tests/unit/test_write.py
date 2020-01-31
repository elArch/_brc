import pytest
import random
import string
from src.Pen import Pen


def random_average_word():
    return ''.join(random.choices(string.ascii_letters +
                                  string.digits, k=random.randint(0, 1000)))


def random_longest_word():
    return ''.join(random.choices(string.ascii_letters +
                                  string.digits, k=random.randint(1001, 2001)))


def test_object_write_average_word():
    pen = Pen()
    avg_word = random_average_word()
    avg_word_size = len(avg_word) * pen.size_letter
    inks = pen.ink_container_value

    if avg_word_size <= pen.ink_container_value:
        assert pen.write(avg_word) == avg_word
        assert pen.ink_container_value == inks - avg_word_size
    else:
        assert pen.write(avg_word) == avg_word[0: pen.ink_container_value]
        assert pen.ink_container_value == 0


def test_object_write_longest_word():
    pen = Pen()
    lng_word = random_longest_word()
    lng_word_size = len(lng_word) * pen.size_letter
    inks = pen.ink_container_value

    if lng_word_size <= pen.ink_container_value:
        assert pen.write(lng_word) == lng_word
        assert pen.ink_container_value == inks - lng_word_size
    else:
        part_lng_word = lng_word[0: pen.ink_container_value]
        assert pen.write(lng_word) == part_lng_word
        assert pen.ink_container_value == 0
