def law_of_large_number(arr, m, k):
    sorted_arr = sorted(arr, reverse=True)  # https://docs.python.org/ko/3/howto/sorting.html

    # 가장 큰 수가 더해지는 횟수
    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    # 횟수 * 가장 큰 수  + (m-횟수) * 두번째로 큰 수
    result = count * sorted_arr[0] + (m - count) * sorted_arr[1]
    return result


def main():
    arr = [2, 4, 5, 4, 6]

    result = law_of_large_number(arr, 8, 3)
    print(result)


if __name__ == '__main__':
    main()
