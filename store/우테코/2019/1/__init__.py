def solve():
    money_units = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    money = int(input())
    for idx, unit in enumerate(money_units):
        result[idx] = int(money / unit)
        money = money % unit

        if 0 == money:
            break

    print(result)


if __name__ == '__main__':
    solve()
