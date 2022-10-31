'''
십자가 이동 시 이전 자리로 못가게 -> visited (사용 전후로 visited 복구시켜줘야 함)
첫 시작점에서 벗어나면서 판단하게 -> distance is not 0 and place == "P" (24줄)

'''

deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]  

def check_adjecent(place, visited, i, j, distance):
    if distance >= 3:
        return 

    if i < 0 or i > 4 or j < 0 or j > 4:
        return 

    if visited[i][j]:
        return

    visited[i][j] = True

    if place[i][j] == "X":
        return 

    if distance is not 0 and place[i][j] == "P":
        return False

    for delta in deltas:
        i_new = i + delta[0]
        j_new = j + delta[1]

        check_result = check_adjecent(place, visited, i_new, j_new, distance+1)

        if check_result == False:
            return False

    visited[i][j] = False

    return True
        
def is_safe(place):
    visited = [[False] * 5 for _ in range(5)]

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                check_result = check_adjecent(place, visited, i, j, 0)
                if check_result == False:
                    return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(is_safe(place))

    return answer




print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
