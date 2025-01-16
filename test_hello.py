from hello import add


def test_add():
    assert 2 == add(1, 1)


def test_var():
    x = 1
    assert 1 == x
