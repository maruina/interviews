from .battleship import validate_coordinates


def test_validate_coordinates():
    assert validate_coordinates(2, 3)
    assert validate_coordinates(0, 0)
    assert not validate_coordinates(11, 2)
    assert not validate_coordinates(3, 12)
    assert not validate_coordinates(23, 45)
