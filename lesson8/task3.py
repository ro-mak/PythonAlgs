# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint


def generate_graph(n):
    g = []
    for i in range(0, n):
        g.append([randint(0, n) for j in range(0, n)])
    for i in range(len(g)):
        print(g[i])
    return g


size = int(input("Graph size: "))
gr = generate_graph(size)


def deep_search(graph, start):
    pass
