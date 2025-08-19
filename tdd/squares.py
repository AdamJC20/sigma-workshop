"""Functions that handle squares."""


def is_valid_square(sides: list[int]) -> bool:
    """Returns True if the sides form a valid square"""

    if len(sides) != 4 or sides[0] <= 0:
        return False

    for side in sides:
        if side != sides[0]:
            return False

    return True
