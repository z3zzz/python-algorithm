from itertools import permutations
import queue

def ctrl(board, cur_x, cur_y, dx, dy):
    for i in range(1, 4):
        if 0 <= (new_x := cur_x + dx * i) < 4 and 0 <= (new_y := cur_y + dy * i) < 4:
            if board[new_x][new_y] > 0:
                return (new_x, new_y)

            maximum = i
    
    return (cur_x + dx * maximum, cur_y + dy * maximum)


def move(board, start, end):
    dist = [[6] * 4 for _ in range(4)]
    q = queue.Queue()
    q.put((start, 0))

    while not q.empty():
        (cur_x, cur_y), cur_dist = q.get()
        if cur_dist < dist[cur_x][cur_y]:
            dist[cur_x][cur_y] = cur_dist
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < 4 and 0 <= next_y < 4:
                    q.put(((next_x, next_y), cur_dist + 1))
                    q.put((ctrl(board, cur_x, cur_y, dx, dy), cur_dist + 1))

    return dist[end[0]][end[1]]

def remove_cards(board, start, target):
    target_location = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                target_location.append((i, j))

    loc_a, loc_b = target_location

    distance1 = move(board, start, loc_a) + 1 + move(board, loc_a, loc_b) + 1,
    distance2 = move(board, start, loc_b) + 1 + move(board, loc_b, loc_a) + 1

    if distance1 < distance2:
        return distance1, loc_b
    else:
        return distance2, loc_a

def solution(board, r, c):
    cards = set()
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards.add(board[i][j])
    perms = list(permutations(cards))

    minimum = 99

    for perm in perms:





print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
