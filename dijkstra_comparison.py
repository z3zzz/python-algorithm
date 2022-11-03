from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(edges, start, end):
    graph = defaultdict(list)
    for l, r, c in edges:
        graph[l].append((r, c))
    
    heap, visited, min_dist = [(0, start, [])], set(), {start: 0}

    while heap:
        cost, vertex, path = heappop(heap)
        if vertex == end:
            return cost, path

        if vertex not in visited:
            visited.add(vertex)
            for neighbor, distance in graph[vertex]:
                cur_distance = min_dist.get(neighbor, None)
                new_distance = cost + distance

                if not cur_distance or new_distance < cur_distance:
                    min_dist[neighbor] = new_distance
                    heappush(heap, (new_distance, neighbor, path + [neighbor] ))
    
    return float("inf"), None






if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("A -> G:")
    print(dijkstra(edges, "A", "G"))
