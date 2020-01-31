from src.Pen import Pen


def test_default_do_something_else(capfd):
    pen = Pen()
    pen.do_something_else()

    out, err = capfd.readouterr()
    assert out == pen.color
