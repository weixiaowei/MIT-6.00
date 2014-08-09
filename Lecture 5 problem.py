#L5 problem 1
def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


#L5 problem 2
def recurPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """

    # exp could be 1, then return base.
    # But to figure out what base case to use,
    # think about what the smallest value of exp can be
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)


#L5 problem 3
def recurPowerNew(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base*recurPowerNew(base, exp-1)
