def solution(record):
    answer = []

    user_dict = {}
    behave_dict = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for word in record:
        word_list = word.split(" ")

        if word_list[0] == "Enter" or word_list[0] == "Change":
            user_dict[word_list[1]] = word_list[2]

    for word in record:
        word_list = word.split(" ")

        if word_list[0] != "Change":
            answer.append(user_dict[word_list[1]] + behave_dict[word_list[0]])

    return answer


if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))
