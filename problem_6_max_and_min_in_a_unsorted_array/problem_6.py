import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == None:
        return None

    min = ints[0]
    max = ints[0]
    for index in range(1, len(ints)):
        if ints[index] < min:
            min = ints[index]

        if ints[index] > max:
            max = ints[index]
    return (min, max)


def test_get_min_max():
    assert get_min_max(None) == None
    assert get_min_max([1]) == (1, 1)
    assert get_min_max([1, 2]) == (1, 2)
    assert get_min_max([2, 1]) == (1, 2)
    assert get_min_max([-1, 1]) == (-1, 1)
    assert get_min_max([-1, -7]) == (-7, -1)

    ## Example Test Case of Ten Integers
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    assert get_min_max(l) == (0, 9)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    print("get_min_max testing complete")


test_get_min_max()
