import math


def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


"""
(25, True)
(18, True)
(10, False)
"""


def area_of_ellipse(x: list):
    data = x.split(",")
    if len(data) == 1:
        area = math.pi * data[0] ** 2
    elif len(data) == 2:
        area = math.pi * data[0] * data[1]
    elif len(data) == 4:
        a = (data[2] - data[0]) / 2
        b = (data[3] - data[1]) / 2
        area = math.pi * a * b
    else:
        area = None
    return area


"""
([1.5], area)
([1.5, 2.5], area)
([1, 10, 20, 30], area)
([1, 2, 3], None)
([], None)
"""
