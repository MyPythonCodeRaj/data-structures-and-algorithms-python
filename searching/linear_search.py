def linear_search(list1, target):
    """
    Return the index position of target if found, else return None
    """
    for i in range(0, len(list1)):
        if list1[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_1 = linear_search(numbers,7)
verify(result_1)

result_2 = linear_search(numbers,11)
verify(result_2)
