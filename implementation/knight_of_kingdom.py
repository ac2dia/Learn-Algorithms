def get_move_case(row, column):
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

    case = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            case += 1

    return case


def main():
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    case = get_move_case(row, column)
    print(case)


if __name__ == '__main__':
    main()
