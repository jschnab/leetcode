from collections import defaultdict, deque
from heapq import heapify, heappop

WHITE = "white"
GRAY = "gray"
BLACK = "black"


class Timer:
    def __init__(self, start=0):
        self.time = start

    def __add__(self, t):
        self.time += t
        return self

    def __str__(self):
        return str(self.time)

    def __repr__(self):
        return str(self)


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = WHITE
        self.parent = None
        self.distance = float("inf")
        self.start = None
        self.end = None
        self.rank = 0

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def root(self):
        cur = self
        while cur is not None and cur.parent is not None:
            cur = cur.parent
        return cur

    def find_set(self):
        if self.parent is not self:
            self.parent = self.parent.find_set()
        return self.parent

    def link(self, other):
        if self.rank > other.rank:
            other.parent = self
        else:
            self.parent = other
            if self.rank == other.rank:
                other.rank += 1

    def union(self, other):
        self.find_set().link(other.find_set())


class Edge:
    def __init__(self, src, dst, weight=None):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        w = ""
        if self.weight is not None:
            w = f"({self.weight})"
        return f"{self.src}->{self.dst}{w}"

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacent = defaultdict(set)
        for e in edges:
            self.adjacent[e.src].add(e)
        self.topo_sorted = []

    def __getitem__(self, item):
        return self.adjacent[item]

    def __str__(self):
        return f"{self.adjacent}"

    def __repr__(self):
        return str(self)

    def reset_distances(self):
        for v in self.vertices:
            v.distance = float("inf")

    def reset_parents(self):
        for v in self.vertices:
            v.parent = None

    def reset_colors(self):
        for v in self.vertices:
            v.color = WHITE

    def reset_ranks(self):
        for v in self.vertices:
            v.rank = 0

    def transpose(self):
        return Graph(self.vertices, [Edge(e.dst, e.src) for e in self.edges])

    def zero_indegree_vertices(self):
        result = set(self.vertices)
        for edge in self.edges:
            result.discard(edge.dst)
        return result

    def bfs(self, start, visit=lambda x: None):
        self.reset_distances()
        self.reset_parents()
        self.reset_colors()
        start.distance = 0
        start.color = GRAY
        q = deque([start])
        while q:
            cur = q.pop()
            visit(cur)
            for edge in self[cur]:
                if edge.dst.color is WHITE:
                    edge.dst.color = GRAY
                    edge.dst.distance = cur.distance + 1
                    edge.dst.parent = cur
                    q.appendleft(edge.dst)
            cur.color = BLACK

    def print_path(self, start, end):
        if start is end:
            print(start)
        elif end.parent is None:
            raise RuntimeError(f"No path from {start} to {end}")
        else:
            self.print_path(start, end.parent)
            print(end)

    def dfs(self, visit=lambda x: None):
        self.topo_sorted = []
        self.timer = Timer()
        self.reset_parents()
        self.reset_colors()
        for v in self.vertices:
            if v.color is WHITE:
                self.dfs_visit(v, visit)

    def dfs_visit(self, vertex, visit):
        visit(vertex)
        self.timer += 1
        vertex.start = self.timer.time
        vertex.color = GRAY
        for edge in self[vertex]:
            if edge.dst.color is WHITE:
                edge.dst.parent = vertex
                self.dfs_visit(edge.dst, visit)
        self.timer += 1
        vertex.end = self.timer.time
        vertex.color = BLACK
        self.topo_sorted.append(vertex)

    def topological_sort(self, method="tarjan"):
        if method == "tarjan":
            self.dfs()
            return self.topo_sorted[::-1]

        elif method == "kahn":
            zero_indegree = self.zero_indegree_vertices()
            rev_adjacent = defaultdict(set)
            for vertex, edges in self.adjacent.items():
                for e in edges:
                    rev_adjacent[e.dst].add(e)
            result = []
            while len(zero_indegree) > 0:
                cur = zero_indegree.pop()
                result.append(cur)
                for edge in self.adjacent[cur]:
                    rev_adjacent[edge.dst].discard(edge)
                    if len(rev_adjacent[edge.dst]) == 0:
                        zero_indegree.add(edge.dst)
            return result

    def strongly_connected_components(self):
        self.dfs()
        T = self.transpose()
        T.vertices = sorted(T.vertices, key=lambda x: x.end, reverse=True)
        T.dfs()
        components = defaultdict(set)
        for v in T.vertices:
            components[v.root()].add(v)
        return list(components.values())

    def kruskal(self):
        for v in self.vertices:
            v.parent = v
        self.reset_ranks()
        self.edges = sorted(self.edges, key=lambda x: x.weight)
        result = []
        for e in self.edges:
            if e.src.find_set() != e.dst.find_set():
                result.append(e)
                e.src.union(e.dst)
        return result

    def prim(self, start):
        for v in self.vertices:
            v.rank = float("inf")
            v.parent = None
        start.rank = 0
        seen = {start}
        q = [(v.rank, i, v) for i, v in enumerate(self.vertices)]
        heapify(q)
        while len(q) > 0:
            *_, cur = heappop(q)
            seen.add(cur)
            for edge in self[cur]:
                if edge.dst not in seen and edge.weight < edge.dst.rank:
                    edge.dst.parent = cur
                    edge.dst.rank = edge.weight


def main():
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    belt = Vertex("belt")
    watch = Vertex("watch")
    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    shoes = Vertex("shoes")
    socks = Vertex("socks")
    V = [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]
    E = [
        Edge(shirt, tie),
        Edge(shirt, belt),
        Edge(tie, jacket),
        Edge(tie, belt),
        Edge(undershorts, pants),
        Edge(undershorts, shoes),
        Edge(pants, belt),
        Edge(pants, shoes),
        Edge(belt, jacket),
        Edge(socks, shoes),
    ]
    G = Graph(V, E)
    print(G.topological_sort())


if __name__ == "__main__":
    main()
