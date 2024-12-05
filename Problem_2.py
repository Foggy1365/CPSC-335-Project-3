import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    #creation of the adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        #for every edge (u -> v) with weight w, add v and w to adjacency list
        graph[u].append((v,w))

    #initialization of min-heap and distances
    pque = [(0,k)] #priority que storing(time, node)
    #initialize distance to infinity
    distances ={i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    #process the graph using Dijkstra's algorithm
    while pque:
        time, node = heapq.heappop(pque)
        if time > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_time = time + weight
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(pque, (new_time, neighbor))

    #result
    max_time = max(distances.values())
    #if max time reaches infinity then some nodes cannot be reached resulting in -1
    return max_time if max_time < float('inf') else -1

times1 = [[2,1,1], [2,3,1], [3,4,1]]
n1, k1 = 4, 2
print("Minimum time for", n1, "nodes:", networkDelayTime(times1, n1, k1))

times2 = [[1,2,1]]
n2, k2 = 2, 1
print("Minimum time for", n2, "nodes:", networkDelayTime(times2, n2, k2))

times3 = [[1,2,1]]
n3, k3 = 2, 2
print("Minimum time for", n3, "nodes:", networkDelayTime(times3, n3, k3))