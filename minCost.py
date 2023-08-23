# Author: Aubrianna Sample
# The purpose of this program is to calculate the minimum cost
# spanning tree given the edges.

import heapq

def minimum_spanning_tree(edges):
    num_nodes = len(edges)
    mst_edges = [[] for _ in range(num_nodes)]  # Stores the edges in the MST.
    visited = [False]*num_nodes  # Tracks which nodes are in the MST.
    min_heap = []  # Use a heap to always get the edge with smallest weight.

    # Start from node 0.
    for end_node, weight in edges[0]:
        heapq.heappush(min_heap, (weight, 0, end_node))

    while min_heap:
        weight, start_node, end_node = heapq.heappop(min_heap)  # Get edge with smallest weight.
        if not visited[end_node]:  # If end_node is not in the MST.
            visited[end_node] = True  # Add end_node to the MST.
            mst_edges[start_node].append([end_node, weight])  # Add edge to the MST.
            mst_edges[end_node].append([start_node, weight])  # Add edge to the MST.

            # Add all edges that start from end_node and go to a node not in the MST.
            for next_node, next_weight in edges[end_node]:
                if not visited[next_node]:
                    heapq.heappush(min_heap, (next_weight, end_node, next_node))

    return mst_edges

edges = [
    [(1, 3), (2, 5)],
    [(0, 3), (2, 10), (3, 12)],
    [(0, 5), (1, 10)],
    [(1, 12)]
]
print(minimum_spanning_tree(edges))
