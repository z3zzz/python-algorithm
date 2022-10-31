'''
range sum -> 양 끝 (n차원 공통) 만 각각 +n, -n 으로 해 놓고
나중에 위->아래 혹은 왼->오른 누적합 구하면 됨

try except pass

'''


def apply_brutal(board, skill):
    attack_heal, r1, c1, r2, c2, degree = skill
    degree = degree if attack_heal == 2 else -degree

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            board[i][j] += degree

    return board

def count_brutal(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                count += 1

    return count

def apply_efficient(helper_board, skill):
    attack_heal, r1, c1, r2, c2, degree = skill
    degree = degree if attack_heal == 2 else -degree

    helper_board[r1][c1] += degree
    
    try:
        helper_board[r1][c2+1] -= degree
    except:
        pass

    try:
        helper_board[r2+1][c1] -= degree
    except:
        pass

    try:
        helper_board[r2+1][c2+1] += degree
    except:
        pass

    return helper_board

def count_efficient(board, helper_board):
    count = 0

    for i in range(1, len(board)):
        for j in range(len(board[0])):
            helper_board[i][j] = helper_board[i][j] + helper_board[i-1][j]
    
    for i in range(0, len(board)):
        for j in range(1, len(board[0])):
            helper_board[i][j] = helper_board[i][j] + helper_board[i][j-1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            score = board[i][j] + helper_board[i][j]

            if score > 0:
                count += 1
    
    return count

def solution(board, skills):
    # for skill in skills:
        # board = apply_brutal(board, skill)

    # answer = count_brutal(board)

    helper_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for skill in skills:
        helper_board = apply_efficient(helper_board, skill)

    answer = count_efficient(board, helper_board)

    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
