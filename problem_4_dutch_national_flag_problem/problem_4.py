def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    last_zero_index = 0
    last_two_index = len(input_list) - 1
    index = 0

    while index < last_two_index:
        value = input_list[index]
        if value == 0:
            input_list[index] = input_list[last_zero_index]
            input_list[last_zero_index] = value
            last_zero_index += 1
            index += 1
        elif value == 2:
            input_list[index] = input_list[last_zero_index]
            input_list[last_two_index] = value
            last_two_index -= 1
        else:
            index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    assert sorted_array == sorted(test_case)
    print("Pass")


def test_sort_012():
    test_function([0])
    test_function([1])
    test_function([2])
    test_function([0, 1, 2])
    test_function([2, 1, 0])
    test_function([2, 0, 1])
    test_function([1, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function(
        [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    )
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


test_sort_012()
