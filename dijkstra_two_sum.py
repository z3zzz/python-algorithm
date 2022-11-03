'''
중간에 겹칠 경우
겹치는 지점까지의 거리 + 거기서 각 도착점까지의 거리들의 합 
brutal로 구하고 최소값 구하면 됨

'''
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(start, end, fares):
    graph = defaultdict(list)
    for l, r, c in fares:
        graph[l].append((r, c))
        graph[r].append((l, c))

    heap, visited, min_dist = [(0, start)], set(), {start: 0}

    while heap:
        cost, vertex = heappop(heap)
        if vertex == end:
            return cost

        if vertex not in visited:
            visited.add(vertex)
            for neighbor, distance in graph[vertex]:
                # 필요함!
                if neighbor in visited: continue
                cur_distance = min_dist.get(neighbor, None)
                new_distance = cost + distance

                if not cur_distance or new_distance < cur_distance:
                    min_dist[neighbor] = new_distance
                    heappush(heap, (new_distance, neighbor))

    return float("inf")



def solution(n, s, a, b, fares):
    answer = float("inf")

    for i in range(1, n+1):
            answer = min(answer, 
    dijkstra(s, i, fares) + dijkstra(i, a, fares) + dijkstra(i, b, fares)
                    )

    return answer

print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))


