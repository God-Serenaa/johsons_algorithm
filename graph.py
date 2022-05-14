class Johnson:
    def __init__(self, v):
        self.vertices = v
        self.graph = []
        self.distance = []
        self.parent = []
        self.path = []

    def addedge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_path(self, d, s):
        self.path.append(d)
        if d == s:
            return self.path[::-1]
        return self.find_path(self.parent[d], s)

    def bellman(self, s):
        d = [float("Inf")] * self.vertices
        self.parent = []
        self.parent = [-1] * self.vertices
        d[s] = 0
        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    self.parent[v] = u
        for u, v, w in self.graph:
            if d[v] > d[u] + w:
                return False
        for i in range(self.vertices):
            if i != s:
                print("->".join(str(x) for x in self.find_path(i, s)) + " Cost:", d[i])
                self.path = []
        return True

    def print_all_path(self):
        for i in range(self.vertices):
            print("source:", i)
            if not self.bellman(i):
                print("Negative Cycle Detected! Aborting process...")
                return
