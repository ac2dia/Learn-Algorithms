def solution(arr):
    answer = []

    counts = []
    for i in range(1, 4):
        counts.append(arr.count(i))

    max_count = max(counts)

    for count in counts:
        answer.append(max_count - count)

    return answer


if __name__ == '__main__':
    arr = [2, 1, 3, 1, 2, 1]
    print(solution(arr))
