'''
n x n 수가 작음 -> brutal force 용 
십자가 deltas -> 0,-1  0,1   -1,0    1,0
번갈아가면서 count -> count 홀짝에 따라 차례 구분
문제의 조건을 그대로 코드로
for delta in deltas 에서 index error, 못가는 곳 continue
board[x][y]=0 에서 작업 후 다시 1로 바꾸어서 복구
움직이고 count + 1 하고 바로 상대방 움직일 차례
'''
deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def move(board, aloc, bloc, count):
    global deltas
    result = []
    is_a_turn = count % 2 == 0 

    if is_a_turn:
        turn = aloc
    else:
        turn = bloc

    if board[turn[0]][turn[1]] == 0:
        return count

    board[turn[0]][turn[1]] = 0

    for delta in deltas:
        x = turn[0] + delta[0]
        y = turn[1] + delta[1]

        if x < 0 or x >= len(board):
            continue
        if y < 0 or y >= len(board[0]):
            continue
        if board[x][y] == 0:
            continue

        if is_a_turn:
            result.append(move(board, [x, y], bloc, count+1))
        else:
            result.append(move(board, aloc, [x, y], count+1))

    board[turn[0]][turn[1]] = 1

    if len(result) == 0:
        return count 

    a_win = []
    b_win = []

    for r in result:
        b_win.append(r) if r % 2 == 0 else a_win.append(r)

    if is_a_turn:
        return max(b_win) if len(a_win) == 0 else min(a_win)
    else:
        return max(a_win) if len(b_win) == 0 else min(b_win)
    
def solution(board, aloc, bloc):
    answer = move(board, aloc, bloc, 0)

    return answer

print(solution(	[[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
