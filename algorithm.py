count = 0


def increase():
    global count
    count += 1


def merge_sort(input_array):
    if len(input_array) == 1:
        return input_array

    middle_pos = int(len(input_array) / 2)
    end_pos = len(input_array)

    left_part = merge_sort(input_array[0:middle_pos])
    right_part = merge_sort(input_array[middle_pos:end_pos])

    return merge(left_part, right_part)


def merge(left_part, right_part):
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
    if abs(max_value-min_value) == 1:
        return max_value

    increase()

    middle_value = (min_value + max_value) // 2
    if is_bananas_per_hour_suitable(middle_value, piles, free_hours, index):
        return binary_search(min_value, middle_value, piles, free_hours, index)
    else:
        return binary_search(middle_value, max_value, piles, free_hours, index)


def count_bananas_per_hour(piles, free_hours):
    pass

