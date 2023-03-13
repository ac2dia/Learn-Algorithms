def solution(n, m, section):
    answer = 0

    end = 0
    for i in section:
        if i < end:
            continue

        answer += 1
        end = i + m

    return answer
