def merge_sort(input_array):
    """
    Sorts array with merge sort method
    Returns sorted array

    >>> merge_sort([-4, 30, 12, 1, 0, 101, 14])
    [-4, 0, 1, 12, 14, 30, 101]
    >>> merge_sort([1, 3, 8, 0, 2, 31, -12])
    [-12, 0, 1, 2, 3, 8, 31]
    >>> merge_sort([239, 1034, -234, 45, 0, 323, -12])
    [-234, -12, 0, 45, 239, 323, 1034]
    """
    if len(input_array) == 1:
        return input_array

    middle_pos = len(input_array) // 2
    end_pos = len(input_array)

    left_part = merge_sort(input_array[0:middle_pos])
    right_part = merge_sort(input_array[middle_pos:end_pos])

    return merge(left_part, right_part)


def merge(left_part, right_part):
    """
    Merges two sorted arrays into one
    Returns merged sorted array

    >>> merge([-5, 10], [0, 15])
    [-5, 0, 10, 15]
    >>> merge([0, 5, 15], [2, 3])
    [0, 2, 3, 5, 15]
    >>> merge([1, 2], [-5, -4])
    [-5, -4, 1, 2]
    """
    left_index = 0
    right_index = 0
    result_array = []

    while (left_index < len(left_part)) and (right_index < len(right_part)):
        if left_part[left_index] <= right_part[right_index]:
            result_array.append(left_part[left_index])
            left_index += 1
        else:
            result_array.append(right_part[right_index])
            right_index += 1

    if left_index < len(left_part):
        result_array.extend(left_part[left_index:])
    if right_index < len(right_part):
        result_array.extend(right_part[right_index:])

    return result_array


def binary_search(min_value, max_value, piles, free_hours, index):
    """
    Returns min number in range from min_value to max_value
    that fits condition of is_bananas_per_hour_suitable

    >>> binary_search(14, 30, [4, 11, 13, 14, 30], 6, 3)
    15
    """
    if abs(max_value-min_value) == 1:
        return max_value

    middle_value = (min_value + max_value) // 2
    if is_bananas_per_hour_suitable(middle_value, piles, free_hours, index):
        return binary_search(min_value, middle_value, piles, free_hours, index)
    else:
        return binary_search(middle_value, max_value, piles, free_hours, index)


def count_bananas_per_hour(piles, free_hours):
    """
    Returns counted quantity on bananas per hour
    >>> count_bananas_per_hour([3, 6, 7, 11], 8)
    4
    >>> count_bananas_per_hour([30, 11, 23, 4, 20], 5)
    30
    >>> count_bananas_per_hour([30, 11, 23, 4, 20], 6)
    23
    >>> count_bananas_per_hour([30, 11, 14, 4, 13], 6)
    15
    >>> count_bananas_per_hour([2, 2], 5)
    1
    """
    sorted_piles = merge_sort(piles)

    if len(sorted_piles) == free_hours:
        return sorted_piles[-1]

    greater_value = sorted_piles[-1]
    last_index = 0
    for index in range(len(sorted_piles) - 2, -1):
        bananas_per_hour = sorted_piles[index]
        smaller_value = bananas_per_hour
        if not is_bananas_per_hour_suitable(bananas_per_hour, sorted_piles, free_hours, index):
            last_index = index
            break
        greater_value = bananas_per_hour
    else:
        smaller_value = 0

    return binary_search(smaller_value, greater_value, sorted_piles, free_hours, last_index)


def is_bananas_per_hour_suitable(bananas_per_hour, piles, free_hours, current_index):
    """
    Returns true if bananas in piles can be eaten in free_hours of faster
    Else returns false

    >>> is_bananas_per_hour_suitable(5, [3, 5, 8], 6, 1)
    True
    >>> is_bananas_per_hour_suitable(1, [2, 2, 2], 5, 0)
    False
    >>> is_bananas_per_hour_suitable(23, [4, 11, 20, 23, 30], 5, 3)
    False
    >>> is_bananas_per_hour_suitable(23, [4, 11, 20, 23, 30], 6, 3)
    True
    """
    total_hours = current_index
    for pile in piles[current_index:]:
        total_hours += (pile // bananas_per_hour) + (1 if (pile % bananas_per_hour) > 0 else 0)
    return total_hours <= free_hours


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
