import graph

v = int(input("enter number of vertices: "))
g = graph.Johnson(v)
for _ in range(int(input("enter number of edges: "))):
    u, v, w = map(int, input().split())
    g.addedge(u, v, w)

g.print_all_path()
