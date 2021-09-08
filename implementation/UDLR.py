def up_down_left_right(n, moves):
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['U', 'D', 'L', 'R']

    for move in moves:
        nx, ny = 1, 1
        for idx in range(len(move_types)):
            if move == move_types[idx]:
                nx = x + dx[idx]
                ny = y + dy[idx]
                break

        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

    return x, y


def main():
    n = int(input())
    moves = input().split()

    x, y = up_down_left_right(n, moves)
    print(x, y)


if __name__ == '__main__':
    main()
