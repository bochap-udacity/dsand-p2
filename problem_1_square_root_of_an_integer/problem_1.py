def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 2:
        return number

    lower = 0
    higher = number // 2

    while lower < higher:
        mid = (lower + higher) // 2
        squared = mid ** 2
        if squared == number:
            return mid
        elif squared < number:
            lower = mid + 1
        else:
            higher = mid - 1
    return higher


def test_sqrt():
    assert sqrt(0) == 0
    print("Pass" if (0 == sqrt(0)) else "Fail")
    assert sqrt(1) == 1
    print("Pass" if (1 == sqrt(1)) else "Fail")
    assert sqrt(2) == 1
    print("Pass" if (1 == sqrt(2)) else "Fail")
    assert sqrt(3) == 1
    print("Pass" if (1 == sqrt(3)) else "Fail")
    assert sqrt(4) == 2
    print("Pass" if (2 == sqrt(4)) else "Fail")
    assert sqrt(9) == 3
    print("Pass" if (3 == sqrt(9)) else "Fail")
    assert sqrt(16) == 4
    print("Pass" if (4 == sqrt(16)) else "Fail")
    assert sqrt(27) == 5
    print("Pass" if (5 == sqrt(27)) else "Fail")
    assert sqrt(35) == 5
    print("Pass" if (5 == sqrt(35)) else "Fail")
    assert sqrt(36) == 6
    print("Pass" if (6 == sqrt(36)) else "Fail")
    assert sqrt(37) == 6
    print("Pass" if (6 == sqrt(37)) else "Fail")


test_sqrt()
