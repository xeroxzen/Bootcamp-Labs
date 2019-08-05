#Fill in your name and surname
name = "Andile"
surname = "Mbele"
assignment = "lab1"

def twenty_nineteen():
    """Come up with the most creative expression that evaluates to 2019,
    using only numbers and the +, *, and - operators.

    >>> twenty_nineteen()
    2019
    """
    year = (10*12)//2+(9-3+12)*8+3-6+(43**2-31)
    return year