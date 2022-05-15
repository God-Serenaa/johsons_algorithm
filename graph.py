class Johnson:
    # initialization
    def __init__(self, v):
        self.vertices = v
        self.graph = []
        self.distance = []
        self.parent = []
        self.path = []

    # adding new edge
    def addedge(self, u, v, w):
        self.graph.append([u, v, w])

    # finding path from source to destination
    def find_path(self, d, s):
        self.path.append(d)
        if d == s:
            return self.path[::-1]
        return self.find_path(self.parent[d], s)

    # bellman-ford
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
        # checking for negative cycle
        for u, v, w in self.graph:
            if d[v] > d[u] + w:
                return False
        # printing the path with cost
        for i in range(self.vertices):
            if i != s:
                print("->".join(str(x) for x in self.find_path(i, s)) + " Cost:", d[i])
                self.path = []
        return True

    # run bellman-ford for each pair
    def print_all_path(self):
        for i in range(self.vertices):
            print("Source:", i)
            if not self.bellman(i):
                print("Negative Cycle Detected! Aborting process...")
                return
        self.transform()

    # removing all negative vertices
    def transform(self):
        add = 0
        for u, v, w in self.graph:
            if w < 0 and add > w:
                add = w
        if add == 0:
            print("\n\nNo negative vertices detected. Transformation not needed.")
        else:
            print("\n\nRemoving negative vertices...\nTransformed graph: ")
            for u, v, w in self.graph:
                print(u, v, w - add)
