def solution(s):
    answer = []

    count = 1
    last_index = len(s) - 1
    for idx in range(0, last_index):

        if s[idx] == s[idx + 1]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.append(count)

    if s[0] == s[last_index]:
        answer[0] = answer[0] + answer[-1]
        del (answer[-1])

    answer.sort()
    return answer


if __name__ == '__main__':
    # s = "aaabbaaa"
    s = "aaabbaac"
    # s = "wowwow"

    print(solution(s))
