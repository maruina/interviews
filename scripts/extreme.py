def extreme(array):
    if not array:
        return -1

    min_ele = max_ele = sum_values = array[0]
    min_idx = max_idx = 0

    for index, value in enumerate(array):
        sum_values += value
        if value < min_ele:
            min_ele = value
            min_idx = index
        elif value > max_ele:
            max_ele = value
            max_idx = index

    mean = sum_values / len(array)
    if mean - min_ele > max_ele - mean:
        return min_idx
    else:
        return max_idx


if __name__ == '__main__':
    a = [9, 4, -3, -10, 2, 3, 4, 9, 30]
    print extreme(a)
