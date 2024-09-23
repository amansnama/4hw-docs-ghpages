# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: int|float, b: int|float, c: int|float) -> int|float:
    """Add three numbers.

    function to sum the 3 numbers

    Input: 3 numbers a, b, c

    Output: the sum of a, b, and c

    author: Aman Shrestha

    date: Sep 20, 2024

    Args:
        a (int | float): Number 1
        b (int | float): Number 2
        c (int | float): Number 3

    Returns:
        int|float: Sum
    """
    # this is the summation
    out = a + b + c

    return out


def my_thermo_stat(temp: int | float, desired_temp: int | float) -> str:
    """Change thermostat setting.

    Changes the status of the thermostat based on 
    temperature and desired temperature

    author: Aman Shrestha

    date: Sep 20, 2024

    Args:
        temp (int | float): Current temperature
        desired_temp (int | float): Temperature to set to.

    Returns:
        str: Status of thermostat
    """ 
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status


def have_digits(s: str) -> int:
    """Checks if string has digits.

    Args:
        s (str): String to check

    Returns:
        out: 1 if s has digits
             0 if s has no digits
    """    

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out
