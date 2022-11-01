class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

def solution(k, num, links):
    nodes = []
    for n in num:
        nodes.append(Node(n))
    for i in range(len(links)):
        link = links[i]
        if link[0] != -1:
            nodes[i].left = link[0]
        if link[1] != -1:
            nodes[i].right = link[0]



    answer = 0
    return answer


print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))




