# Triangle Angle/Sides Validation in Python | Coding Interview Question
"""
def is_triangle_possible_with_ang(_ang1, _ang2, _ang3):
    if (
        _ang1>0 and
        _ang2>0 and
        _ang3>0 and
        (_ang1+_ang2+_ang3==180)
    ):
        return 'yes'
    return'no'

_result = is_triangle_possible_with_ang(40,60,80)
print(_result)"""

"""def is_triangle_possible_with_side(_side1, _side2, _side3):
    if (
        _side1+_side2>_side3 and
        _side1+_side3>_side2 and
        _side3+_side2>_side1
    ):
        return 'yes'
    return 'no'"""

def is_triangle_possible_with_side(*_sides):
    _tri_side = sorted(_sides)
    if (
        _tri_side[0] + _tri_side[1] > _tri_side[2]
    ):
        return 'yes'
    return 'no'

_result = is_triangle_possible_with_side(4, 5, 23)
print(_result)