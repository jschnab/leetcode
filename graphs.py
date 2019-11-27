# script which implements a graph class

import collections

class Graph(object):
    """Graph objects represented with adjacency lists."""
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        """Add edge u -> v."""
        self.graph[u].append(v)

    #==========================#
    #=== DEPTH-FIRST SEARCH ===#
    #==========================#
    def dfs_util(self, v, visited):
        """Function used by depth-first search."""
        # mark current node as visited and print it
        visited[v] = True
        print(v)
        # recur for all vertices adjecent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs_traversal(self):
        """Function to perform depth-first search traversal."""
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited)

    #===========================#
    #=== TOPOLOGICAL SORTING ===#
    #===========================#
    def topo_sort_util(self, v, visited, stack):
        """Function used by topological search."""
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topo_sort_util(i, visited, stack)
        stack.insert(0, v)

    def topo_sort(self):
        """Function to perform topological sort."""
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topo_sort_util(i, visited, stack)
        print(stack)

    #=======================#
    #=== CYCLE DETECTION ===#
    #=======================#
    def is_cyclic_util(self, v, visited, stack):
        """Function used by cycle detection."""
        # make current node as visited and add to recursion stack
        visited[v] = True
        stack[v] = True
        # recur for all neighbours
        # if vertex is visited and in stack
        # then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_util(neighbour, visited, stack) == True:
                    return True
            elif stack[neighbour] == True:
                return True
        # vertex needs to be popped from recursion stack
        # before recursion ends
        stack[v] = False
        return False

    def is_cyclic(self):
        """Function to detect if graph has cycle."""
        visited = [False] * self.V
        stack = [False] * self.V
        for v in range(self.V):
            if visited[v] == False:
                if self.is_cyclic_util(v, visited, stack) == True:
                    return True
        return False

if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 0)
    g.add_edge(5, 2)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
