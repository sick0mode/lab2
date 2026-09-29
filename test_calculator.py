from calculator import add, divide, is_even


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_even():
    assert is_even(4) is True