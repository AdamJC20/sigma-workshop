"""Tests for triangle.py"""

from triangle import is_valid_triangle
from triangle import is_valid_equilateral_triangle


def test_is_valid_triangle_input_1():

    data = [30, 60, 90]

    result = is_valid_triangle(data)

    assert result == True


def test_is_valid_triangle_input_2():

    data = [30, 30, 30, 30, 30, 30]

    result = is_valid_triangle(data)

    assert result == False


def test_is_valid_triangle_input_3():

    data = [0, 0, 0]

    result = is_valid_triangle(data)

    assert result == False


def test_is_valid_triangle_input_4():

    data = [-1, -3, 10]

    result = is_valid_triangle(data)

    assert result == False


def test_is_valid_equilateral_triangle_input_1():

    data = [60, 60, 60]

    result = is_valid_equilateral_triangle(data)

    assert result == True
