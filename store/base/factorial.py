def factorial_iterative(n): # 반복문으로 구현한 팩토리얼 함수
    result = 1

    for i in range(1, n + 1):
        result *= n

    return result


def factorial_recursive(n): # 재귀로 구현한 팩토리얼 함수
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    print(factorial_iterative(5))
    print(factorial_recursive(5))


if __name__ == '__main__':
    main()
