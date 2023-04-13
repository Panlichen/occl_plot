def calc_bar_pos(num_bar, x, index, width):
    if num_bar == 2:
        start = x - 0.5 * width
    elif num_bar == 3:
        start = x - width
    elif num_bar == 4:
        start = x - 1.5 * width

    for i in range(index):
        start += width

    return start