def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list.sort(reverse=True)
    left_sum = 0
    left_offset = 0
    right_sum = 0
    right_offset = 0
    for index in range(len(input_list)):
        if index % 2 == 0:
            left_sum = left_sum * (10 ** left_offset) + input_list[index]
            left_offset = 1
        else:
            right_sum = right_sum * (10 ** right_offset) + input_list[index]
            right_offset = 1

    return [left_sum, right_sum]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


def test_rearrange_digits():
    assert rearrange_digits([1, 2, 3, 4, 5]) == [531, 42]
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    assert rearrange_digits([4, 6, 2, 5, 9, 8]) == [964, 852]
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    assert rearrange_digits([1, 1]) == [1, 1]
    test_function([[1, 1], [1, 1]])
    assert rearrange_digits([2, 1]) == [2, 1]
    test_function([[2, 1], [2, 1]])
    assert rearrange_digits([1, 0]) == [1, 0]
    test_function([[1, 0], [1, 0]])
    assert rearrange_digits([5, 6, 9, 9, 8, 4, 3, 1, 0]) == [98530, 9641]
    test_function([[5, 6, 9, 9, 8, 4, 3, 1, 0], [98530, 9641]])


test_rearrange_digits()
