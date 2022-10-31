from itertools import combinations_with_replacement

global winning_combination
global score

score = 0

def convert(raw_combinations):
    result = []
    for i in range(10, -1, -1):
        result.append(raw_combinations.count(i))

    return result

def get_combinations(n):
    combinations = []
    raw_combinations = combinations_with_replacement([x for x in range(10, -1, -1)], n)

    for c in raw_combinations:
        combinations.append(convert(list(c)))
    
    return combinations

def get_one(n):
    if n == 0: return -1
    return n // abs(n)

def calculate_score(info, combination):
    global winning_combination
    global score
    cur_score = 0
    for i in range(11):
        if (info[i] == 0 and combination[i] == 0): continue
        cur_score += get_one(combination[i] - info[i]) * (10 - i)

    if cur_score > score:
        winning_combination = combination
        score = cur_score
    elif cur_score == score and winning_combination:
        winning_combination = compare_combinations(winning_combination, combination)

def compare_combinations(c1, c2):
    for i in range(10, -1, -1):
        if c1[i] == c2[i]:
            continue
        if c1[i] > c2[i]:
            return c1
        else:
            return c2

def solution(n, info):
    global winning_combination
    global score

    possible_combinations = get_combinations(n)

    for c in possible_combinations:
        calculate_score(info, c)

    if score > 0:
        return winning_combination
    else:
        return [-1]

print(solution(1, [1, 1, 6, 1, 0, 1, 1, 7, 0, 1, 8]))
print(score)

for k in range(1, 11):
    print(k)
    cs = get_combinations(k)
    for c in cs:
        print(c)
        solution(k, c)

#print(calculate_score([2,1,1,1,0,0,0,0,0,0,0], [0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0]))
