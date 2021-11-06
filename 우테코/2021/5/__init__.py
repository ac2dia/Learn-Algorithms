def is_stop_filling(answer, rows, columns, recent_number):
    # case 2
    if rows == columns and rows + columns == recent_number:
        return True

    # case 1
    for row in answer:
        if 0 != row.count(0):
            return False

    return True


def solution(rows, columns):
    answer = [[0] * columns for i in range(rows)]

    r, c = 0, 0
    recent_number = 1

    answer[0][0] = recent_number

    while not is_stop_filling(answer, rows, columns, recent_number):

        if 1 == recent_number % 2:
            recent_number += 1

            c += 1
            if columns == c:
                c = 0
        elif 0 == recent_number % 2:
            recent_number += 1

            r += 1
            if rows == r:
                r = 0

        answer[r][c] = recent_number

    return answer


if __name__ == '__main__':
    # print(solution(3, 4))
    # [[8, 2, 13, 14], [16, 10, 4, 15], [17, 11, 12, 6]]
    print(solution(3, 3))
    # [[1, 2, 0], [0, 3, 4], [6, 0, 5]]
