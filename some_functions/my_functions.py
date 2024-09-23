# Functions for examples_tests.py, renamed to test_example.py

def area_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Calculates area of rectangle.

    Args:
        width (int | float): width of rectangle
        height (int | float): height of rectangle

    Returns:
        int | float: area = width times height
    """
    return width*height


def perimeter_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Calculates perimeter of a rectangle

    Args:
        width (int | float): width of rectangle
        height (int | float): height of rectangle

    Returns:
        int | float: perimeter = 2 * (width + height)
    """
    return 2*(width+height)
