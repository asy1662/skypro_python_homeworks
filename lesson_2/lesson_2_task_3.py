import math

def square(side):
    area = side * side
    if not isinstance(area, int):
        area = math.ceil(area)
    return area