from collections import defaultdict, deque

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

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return all(
            [
                self.value == other.value,
                self.color == other.color,
                self.parent == other.parent,
                self.distance == other.distance,
                self.start == other.start,
                self.end == other.end,
            ]
        )

    def __hash__(self):
        return hash(self.value)


class Edge:
    def __init__(self, src, dst, weight=None):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        w = ""
        if self.weight is not None:
            w = f" {self.weight}"
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


def main():
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    V = [a, b, c, d]
    E = [Edge(a, b), Edge(a, c), Edge(c, d)]
    G = Graph(V, E)
    G.dfs()
    for v in G.vertices:
        print(f"{v} {v.start} {v.end}")


if __name__ == "__main__":
    main()
