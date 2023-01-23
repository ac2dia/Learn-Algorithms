def become_to_number_1(n, k):  # 해당 케이스의 경우 n = 2k-1, k = k 라면 k번 만큼의 반복문을 수행하게 된다.
    count = 0
    while 1 < n:
        if 0 == n % k:
            n /= k
        else:
            n -= 1
        count += 1

    return count


def solve(n, k):
    result = 0

    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        # n을 k로 나눈 몫에 k를 다시 곱한다 -> n이 k로 나눠떨어지지 않을때 가장 가까운 나눠 떨어지는 수를 구할 수 있다.
        target = (n // k) * k
        # 총 연산을 수행하는 횟수 (result) - target 은 1을 처리한 개수를 한번에 구한 것이다.
        result += (n - target)
        n = target

        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break

        # K로 나누기
        result += 1  # k를 나누는 연산을 수행하므로 1번 추가
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1)

    return result


def main():
    n, k = map(int, input().split())

    # result = become_to_number_1(n, k)
    result = solve(n, k)
    print(result)


if __name__ == '__main__':
    main()
