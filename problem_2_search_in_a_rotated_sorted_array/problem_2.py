def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    right_end_index = len(input_list) - 1
    left_end_index = right_end_index // 2
    right_start_index = left_end_index + 1
    left_start_index = 0

    while input_list[left_start_index] > input_list[left_end_index]:
        left_mid_index = (left_start_index + left_end_index) // 2
        if input_list[left_mid_index] < input_list[left_start_index]:
            left_end_index = left_mid_index - 1
            right_start_index = left_mid_index
        else:
            left_end_index = left_mid_index
            right_start_index = left_mid_index + 1

    while input_list[right_start_index] > input_list[right_end_index]:
        right_mid_index = (right_start_index + right_end_index) // 2
        if input_list[left_start_index] < input_list[right_mid_index]:
            left_end_index = right_mid_index
            right_start_index = left_end_index + 1
        else:
            left_end_index += 1
            right_start_index = left_end_index + 1

    start_index = left_start_index
    end_index = left_end_index
    if number < input_list[start_index] or number > input_list[end_index]:
        start_index = right_start_index
        end_index = right_end_index

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if number == input_list[mid_index]:
            return mid_index
        elif number < input_list[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_rotated_array_search():
    assert rotated_array_search([], 2) == -1
    test_function([[], 2])
    assert rotated_array_search([0], 1) == -1
    test_function([[0], 1])
    assert rotated_array_search([0], 0) == 0
    test_function([[0], 0])
    assert rotated_array_search([2, 1], 2) == 0
    test_function([[2, 1], 2])
    assert rotated_array_search([2, 1], 1) == 1
    test_function([[2, 1], 1])
    assert rotated_array_search([2, 1], 3) == -1
    test_function([[2, 1], 3])
    assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6) == 0
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    assert rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1) == 5
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    assert rotated_array_search([2, 3, 4, 6, 7, 8, 9, 10, 1], 1) == 8
    test_function([[2, 3, 4, 6, 7, 8, 9, 10, 1], 1])
    assert rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8) == 2
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    assert rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1) == 3
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    assert rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10) == -1
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])


test_rotated_array_search()
