def count_3_in_time(n):
    # 00:00:00 ~ n:59:59

    count = 0
    for hrs in range(0, n + 1):
        for min in range(0, 60):
            for sec in range(0, 60):
                if -1 != str(hrs).find('3') or -1 != str(min).find('3') or -1 != str(sec).find('3'):
                    count += 1

    return count


def main():
    n = int(input())
    count = count_3_in_time(n)
    print(count)


if __name__ == '__main__':
    main()
