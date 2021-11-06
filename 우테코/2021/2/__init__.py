from datetime import datetime, timedelta


def solution(log):
    answer = ''

    time_format = "%H:%M"
    total_time = timedelta()

    for idx in range(0, len(log), 2):
        start = datetime.strptime(log[idx], time_format)
        end = datetime.strptime(log[idx + 1], time_format)

        study_minute = end - start
        if study_minute < timedelta(minutes=5):
            pass
        elif timedelta(hours=1, minutes=45) < study_minute:
            total_time += timedelta(hours=1, minutes=45)
        else:
            total_time += study_minute

    string_total_time = str(total_time)
    answer = string_total_time.split(":")[0].zfill(2) + ":" + string_total_time.split(":")[1].zfill(2)

    return answer


if __name__ == '__main__':
    log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
    print(solution(log))

