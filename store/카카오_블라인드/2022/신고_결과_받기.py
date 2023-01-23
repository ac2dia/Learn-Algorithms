def solution(id_list, report, k):
    answer = [0] * len(id_list)

    id_dict = {}
    id_count = {}
    for id in id_list:
        id_dict[id] = set()
        id_count[id] = 0

    for r in report:
        reporter, reported_person = r.split(' ')

        reported_set = id_dict[reporter]
        reported_set.add(reported_person)
        id_dict[reporter] = reported_set

    for key, value in id_dict.items():
        for val in value:
            id_count[val] += 1

    index = 0
    for key, value in id_dict.items():
        for val in value:
            if id_count[val] >= k:
                answer[index] += 1

        index += 1

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2

    print(solution(id_list, report, k))
