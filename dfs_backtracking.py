'''
backtracking: moves 배열에 child 넣고, for loop 돌면 됨. 
그러면 child 차례에서 child 이후에 moves 배열에 있던 이전 node로 되돌아감
한 번 갔던 곳을 다시 지나가도 side effect가 없기 때문

갔던 곳 remove를 한다면 array보다 set이 time complexity 낮음


'''


answer = 0

def dfs(graph, info, move, moves, sheep, wolf):
    global answer

    sheep += info[move] ^ 1
    wolf += info[move]

    if sheep <= wolf:
        return

    answer = max(answer, sheep)

    for child in graph[move]:
        moves.add(child)

    for move in moves:
        dfs(graph, info, move, moves - set([move]), sheep, wolf)

    return


def solution(info, edges):
    graph = {x:[] for x in range(len(info))}
    for edge in edges:
        graph[edge[0]].append(edge[1])

    dfs(graph, info, 0, set(), 0, 0)    
        
    global answer

    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], 	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
