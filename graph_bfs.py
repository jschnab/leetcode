#!/usr/bin/env python3

# this script implements a breadth-first search on a non-directed graph
# and records the distance of each node to a source and its predecessor
# along the shortest path to the source
# the following algorithm runs in O(V + E)

from queue import Queue

def BFS(graph, source):
    """Perform breadth-first search on a graph, starting from source
and records distance to source and predecessor."""
    
    # list to record distance to source and predecessors for each node
    bfsInfo = [None] * len(graph)

    for i in range(len(graph)):
        bfsInfo[i] = {'distance': None, 'predecessor': None}

    bfsInfo[source]['distance'] = 0

    q = Queue()
    q.put(source)

    # traverse the graph
    while not q.empty():
        current = q.get()

        for i in range(len(graph[current])):
            neighbour = graph[current][i]

            if not bfsInfo[neighbour]['distance']:
                bfsInfo[neighbour]['distance'] = bfsInfo[current]['distance'] + 1
                bfsInfo[neighbour]['predecessor'] = current
                q.put(neighbour)

    return bfsInfo

adjacent_list = [
        [1],
        [0, 4, 5],
        [3, 4, 5],
        [2, 6],
        [1, 2],
        [1, 2, 6],
        [3, 5],
        []
        ]

bfsInfo = BFS(adjacent_list, 3)
for i in range(len(adjacent_list)):
    print(f"vertex {i} : distance = {bfsInfo[i]['distance']}, \
predecessor = {bfsInfo[i]['predecessor']}")
