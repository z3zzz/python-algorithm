'''
시간 차이: 그냥 h2 - h1 * 60 + m2 - m1
elem 수에 한계 (0000~9999 등) -> array index로 활용 가능
func 내에 global 변수 사용 -> global declaration 필수
math.ceil, enumerate

'''
import math

global time_ins
global time_total

time_ins = [-1] * 10000
time_total = [0] * 10000

def calculate_fee(mins, base_time, base_fee, unit_time, unit_fee):
    if mins <= base_time:
        return base_fee
    return base_fee + math.ceil((mins - base_time) / unit_time) * unit_fee

def time_difference(t1, t2):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))

    return (h2 - h1) * 60 + (m2 - m1)

def parse_record(record):
    global time_ins
    global time_total

    time, car_number, in_out = record.split()
    car_number = int(car_number)

    if in_out == "IN":
        time_ins[car_number] = time
    else:
        time_in = time_ins[car_number]
        time_total[car_number] += time_difference(time_in, time)
        time_ins[car_number] = -1

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees

    for record in records:
        parse_record(record)

    for i, time in enumerate(time_ins):
        if time != -1:
            time_total[i] += time_difference(time, '23:59')

    answer = []

    for time in time_total:
        if time == 0: continue
        answer.append(calculate_fee(time, base_time, base_fee, unit_time, unit_fee))
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))