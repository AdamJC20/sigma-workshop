"""Tests for the functions in squares.py"""

from squares import is_valid_square


def test_is_valid_square_valid_true_input_1():

    # Arrange
    data = [4, 4, 4, 4]

    # Act
    result = is_valid_square(data)

    # Assert
    assert result == True


def test_is_valid_square_valid_true_input_2():

    data = [1, 1, 1, 1]

    result = is_valid_square(data)

    assert result == True


def test_is_valid_square_valid_false_input_1():

    data = [1, 2, 3, 4]

    result = is_valid_square(data)

    assert result == False


def test_is_valid_square_valid_false_input_1():

    data = [1, 1, 1]

    result = is_valid_square(data)

    assert result == False


def test_is_valid_square_valid_false_input_2():

    data = [0, 0, 0, 0]

    result = is_valid_square(data)

    assert result == False
