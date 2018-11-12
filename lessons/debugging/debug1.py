from math import sqrt


def the_next_square_root(n):
    """
    Given an integer n, if n is a perfect square (where the square root of the number is also and integer),
    then return the next perfect square, if it is not a perfect square return the previous perfect square.

    the_next_square_root(3) -> 1
    the_next_square_root(4) -> 9
    the_next_square_root(68) -> 64

    :param n: int
    :return: int
    """
    if sqrt(n) - int(sqrt(n)) == 0:
        return (sqrt(n) + 1) ** 2

    else:
        return (int(sqrt(n))) ** 2


def how_good_are_you(class_points, your_points):
    """
    There was a test in your class and you passed it. Congratulations!
    But you're an ambitious person. You want to know if you're better than the average student in your class.
    You got an array with your colleges' points. Now calculate the average to your points!

    If you are equal to the average return false
    :param class_points: list
    :param your_points: int
    :return: a boolean true if you are better than class average and false if you are worse than class average.
    """

    total_points = sum(class_points)
    if total_points <= your_points:
        return True

    elif your_points >= total_points:
        return False


