"""Lab 2: Expressions and Control Structures"""

#Fill in your name and surname
name = "Andile & Lavender Zandile"
surname = "Mbele & Tshuma"
assignment = "lab2"

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if x > 0 and y > 0:
	    return True
    else:
	    return False

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """

    """Sum_digits using iteration"""
    total = 0
    while n > 10:
        remainder = n % 10
        total += remainder
        n = n // 10
    return total + n

    "*** DONE ***"
















