# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint
from collections import deque


def generate_graph(n):
    g = []
    for i in range(0, n):
        l = [randint(0, 1) for j in range(0, n)]
        if 0 not in l:
            l[n - 1] = 0
        if 1 not in l:
            l[n - 1] = 1
        g.append(l)
    for i in range(len(g)):
        print(g[i])
    return g


size = int(input("Graph size: "))
gr = generate_graph(size)


def deep_search(graph, start):
    visited_nodes = deque()
    nodes_to_visit = deque()
    next_node = start
    while len(visited_nodes) < len(graph):
        visited_nodes.append(next_node)
        child_nodes = graph[next_node]
        for index, node in enumerate(child_nodes):
            if index == next_node:
                continue
            if index not in visited_nodes and node == 1:
                nodes_to_visit.append(index)
        if len(nodes_to_visit) > 0:
            next_node = nodes_to_visit.pop()
        else:
            break
    return visited_nodes


s = int(input("Start: "))
print(deep_search(gr, s))
