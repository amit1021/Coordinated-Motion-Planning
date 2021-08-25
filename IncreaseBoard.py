def row_space(number_of_robots, n):
    # Finds how many lines to add to the board
    row_space = 0
    squares = 0
    while number_of_robots > 0:
        number_of_robots -= (n - squares) * 4
        squares += 2
        row_space += 1
    return row_space + 2


def row_space_final(number_of_robots, n, squares):
    # Finds how many lines to add to the board
    row_space = 0
    squares -= 2
    while number_of_robots > 0:
        number_of_robots -= (n - squares) * 4
        row_space += 1
    return row_space
