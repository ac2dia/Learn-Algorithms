def solution(grid, clockwise):
    answer = ["" for i in range(len(grid))]

    length = len(grid) - 1

    if clockwise:
        for rows in range(length + 1):

            row = length
            col = (row - rows) * 2

            for cols in range(2 * (length - rows) + 1):
                answer[length - rows] += grid[row][col]

                if cols % 2 == 0:
                    row += 0
                    col += -1
                else:
                    row += -1
                    col += -1

    else:
        for rows in range(length + 1):

            row = length - rows
            col = row * 2

            for cols in range(2 * rows + 1):
                answer[rows] += grid[row][col]

                if cols % 2 == 0:
                    row += 1
                    col += 1
                else:
                    row += 0
                    col += -1

    return answer


if __name__ == '__main__':
    # grid = ["1", "234", "56789"]
    grid = ["A", "MAN", "DRINK", "WATER11"]
    clockwise = False
    print(solution(grid, clockwise))
