def solution(time, plans):
    answer = ''

    fri_end = 18
    mon_start = 13

    for plan in plans:
        if "PM" in plan[1]:
            plan_start = int(plan[1][:-2]) + 12
        else:
            plan_start = int(plan[1][:-2])

        if "PM" in plan[2]:
            plan_end = int(plan[2][:-2]) + 12
        else:
            plan_end = int(plan[2][:-2])

        if 0 < fri_end - plan_start:
            time -= fri_end - plan_start
        if 0 < plan_end - mon_start:
            time -= plan_end - mon_start

        if time < 0:
            break
        else:
            answer = plan[0]

    return answer


if __name__ == '__main__':
    time = 3.5
    plans = [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]
    print(solution(time, plans))
