def merge_sort(input_array):
    if len(input_array) == 1:
        return input_array

    middle_pos = len(input_array) // 2
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

    middle_value = (min_value + max_value) // 2
    if is_bananas_per_hour_suitable(middle_value, piles, free_hours, index):
        return binary_search(min_value, middle_value, piles, free_hours, index)
    else:
        return binary_search(middle_value, max_value, piles, free_hours, index)


def count_bananas_per_hour(piles, free_hours):
    sorted_piles = merge_sort(piles)

    if len(sorted_piles) == free_hours:
        return sorted_piles[-1]

    greater_value = sorted_piles[-1]
    last_index = 0
    for index in range(len(sorted_piles) - 2, -1):
        increase()
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
    total_hours = current_index
    for pile in piles[current_index:]:
        total_hours += (pile // bananas_per_hour) + (1 if (pile % bananas_per_hour) > 0 else 0)
    return total_hours <= free_hours
