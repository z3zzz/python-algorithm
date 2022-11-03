import time

def convert_time_to_seconds(time):
    h, m, s = list(map(int, time.split(":")))
    return h * 3600 + m * 60 + s

def apply_play_time(log, plays):
    start, end = log.split("-")
    start_second = convert_time_to_seconds(start)
    end_second = convert_time_to_seconds(end)

    plays[start_second] += 1

    if end_second < len(plays) - 2:
        plays[end_second + 1] -= 1

def apply_accumulated_sum(plays):
    for i in range(1, len(plays)):
        plays[i] = plays[i] + plays[i-1]

def get_best_adv(plays, adv_time):
    seconds = convert_time_to_seconds(adv_time)

    partial_sum = 0
    for i in range(seconds + 1):
        partial_sum += plays[i]

    max_play_time = partial_sum
    max_start_time = 0
    for i in range(seconds + 1, len(plays)):
        partial_sum = partial_sum - plays[i - seconds - 1] + plays[i]
        if partial_sum > max_play_time:
            max_play_time = partial_sum
            max_start_time = i - seconds
        
    return time.strftime('%H:%M:%S', time.gmtime(max_start_time))

def solution(play_time, adv_time, logs):
    plays = [0] * (convert_time_to_seconds(play_time) + 1)

    for log in logs:
        apply_play_time(log, plays)

    apply_accumulated_sum(plays)
    
    return get_best_adv(plays, adv_time)

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
