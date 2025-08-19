def is_valid_triangle(angles: list[int]) -> bool:
    """Returns true if angles form a valid triangle"""
    if len(angles) != 3:
        return False

    x = 0

    for angle in angles:
        if angle <= 0:
            return False

        x += angle

    if x != 180:
        return False

    return True


def is_valid_equilateral_triangle(angles: list[int]) -> bool:
    """Returns True if angles form a valid equilateral triangle"""

    for angle in angles:
        if angle != 60:
            return False

    return True


def get_triangle_type(angles: list[int]) -> bool:
    """Returns the type of triangle as string"""

    d = {}
    for angle in angles:
        d[angle] += 1
    if len(d.values()) == 1:
        return "equilateral"

    elif len(d.values()) == 2:
        return "isosceles"

    elif len(d.values()) == 3:
        return "scalene"
