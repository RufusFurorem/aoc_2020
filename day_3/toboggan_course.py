def count_tree_encounters(toboggan_area, w_slope, h_slope):
    trees_encountered = 0
    h = 0
    w = 0

    # While we have not reached the bottom, continue counting trees
    while h < (len(toboggan_area)):
        try:
            if toboggan_area[h][w] == '#':
                trees_encountered += 1
        except IndexError:
            # Increment the exit condition
            h += h_slope
        h += h_slope
        w += w_slope

    return trees_encountered


if __name__ == '__main__':

    total_value = 1
    with open('..\\toboggan_course.txt', 'r') as fd:
        toboggan_area = fd.read().split('\n')

    # Simple but not efficient logic for extending area
    for i, val in enumerate(toboggan_area):
        toboggan_area[i] = val * len(toboggan_area)

    slope_list = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for slopes in slope_list:
        total_value *= count_tree_encounters(toboggan_area, slopes[0], slopes[1])
    print(total_value)
