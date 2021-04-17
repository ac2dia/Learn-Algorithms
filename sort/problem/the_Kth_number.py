def solution(array, commands):
    answer = []

    for command in commands:
        slice_array = array[command[0] - 1:command[1]]
        slice_array.sort()

        if len(slice_array) < command[2]:
            answer.append(slice_array[-1])
        else:
            answer.append(slice_array[command[2] - 1])

    return answer