'''
permutations -> AA, BB 가능 
combinations -> AB 
string 오름차순 -> sorted(word)

'''
from itertools import combinations
from string import ascii_uppercase

def get_combinations(order, n):
    return [''.join(i) for i in combinations(order, n)]

def best_course(orders, n):
    counts = {}
    for order in orders:
        for c in get_combinations(sorted(order), n):
            counts[c] = counts.get(c, 0) + 1

    max_count = 0
    max_results = []

    for combination, count in counts.items():
        if count <= 1:
            continue
        if count > max_count:
            max_count = count
            max_results = [combination]
        elif count == max_count:
            max_results.append(combination)
    
    return max_results

def solution(orders, course):
    answer = []
    for n in course:
        answer += best_course(orders, n)
    answer.sort()

    return answer

print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))
