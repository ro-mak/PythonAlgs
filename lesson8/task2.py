# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from random import randint


class Vertex:
    def __init__(self, cost, path):
        self.cost = cost
        self.path = path

    def __repr__(self):
        return f"{self.cost} {self.path}"


g = [[0, 0, 1, 1, 9, 0, 0, 0],
     [0, 0, 9, 4, 0, 0, 5, 0],
     [0, 9, 0, 0, 3, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 7, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 2, 0]]

for i in range(len(g)):
    print(g[i])


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = []
    for i in range(0, length):
        cost.append(Vertex(cost=float('inf'), path=[]))
    parent = [-1] * length

    cost[start].cost = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i].cost > vertex + cost[start].cost:
                    cost[i].cost = vertex + cost[start].cost
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i].cost and not is_visited[i]:
                min_cost = cost[i].cost
                start = i
    for i in range(length):
        p = parent[i]
        while p != start and p != -1:
            cost[i].path.append(p)
            p = parent[p]
        cost[i].path.reverse()
        cost[i].path.append(i)
    return cost


s = int(input("Start: "))
print(dijkstra(g, s))
