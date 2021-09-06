def number_card_game(n, m, arr):
    max_value = -1
    for i in range(0, n):
        min_value = min(arr[i])
        max_value = max(max_value, min_value)

    return max_value


def main():
    n, m = map(int, input().split())

    arr = []
    for i in range(0, n):
        arr.append(list(map(int, input().split())))

    result = number_card_game(n, m, arr)
    print(result)


if __name__ == '__main__':
    main()
