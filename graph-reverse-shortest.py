'''
다익스트라 -> heapq


'''
import math

minimum = math.inf

class Node:
    def __init__(self, n):
        self.n = n
        self.ins = {}
        self.outs = {}
        self.is_trap = False
    def reverse_all(self):
        temp = self.ins
        self.ins = self.outs
        self.outs = temp
    def reverse_ins(self, n):
        weight = self.ins[n]
        del self.ins[n]
        self.outs[n] = weight
    def reverse_outs(self, n):
        weight = self.outs[n]
        del self.outs[n]
        self.ins[n] = weight
    def reverse(self, nodes):
        for outs, _ in self.outs.items():
            nodes[outs].reverse_ins(self.n)
        for ins, _ in self.ins.items():
            nodes[ins].reverse_outs(self.n)
        self.reverse_all()

    def print(self):
        print()
        print(self.n)
        for num, weight in self.ins.items():
            print(f"{self.n} <- {num}: {weight}")
        for num, weight in self.outs.items():
            print(f"{self.n} -> {num}: {weight}")
        print(self.is_trap)

def traverse(nodes, prev, cur, goal, score):
    global minimum
    print("AAA", cur.n, goal.n, score)
    if cur == goal:
        minimum = min(minimum, score)
        return
    
    if cur.is_trap:
        cur.reverse(nodes)

    cur.print()

    
    temp = []
    for to_node, weight in cur.outs.items():
        temp.append((to_node, weight))

    for to_node, weight in temp:
        print("BBB", cur.n, to_node, weight)
        if not cur.is_trap and prev.n == to_node:
            continue
        traverse(nodes, cur, nodes[to_node], goal, score + weight)

    return


def solution(n, start, end, roads, traps):
    nodes = [0]
    for i in range(1, n+1):
        nodes.append(Node(i))
    start_node = nodes[start]
    end_node = nodes[end]

    for road in roads:
        from_node, to_node, weight = road
        cur_weight = nodes[from_node].outs.get(to_node, 3001)
        if weight < cur_weight:
            nodes[from_node].outs[to_node] = weight
            nodes[to_node].ins[from_node] = weight

    for trap in traps:
        nodes[trap].is_trap = True

    traverse(nodes, start_node, start_node, end_node, 0)

    global minimum

    return minimum

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
