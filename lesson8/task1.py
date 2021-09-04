from collections import deque

# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = int(input("Number of friends: "))

graph = []

for i in range(0, n):
    graph.append([1 if j != i else 0 for j in range(0, n)])
for i in graph:
    print(i)
handshakes = 0
iter = 0

for i in range(len(graph)):
    for j in range(i + 1, len(graph[i])):
        item1 = graph[i][j]
        item2 = graph[j][i]
        print(f"Checking item1[{i},{j}] and item2[{j},{i}]")
        iter += 1
        if item1 == item2 and item1 == 1:
            handshakes += 1
            graph[i][j] = 0
print(f"Handshakes = {handshakes}")
print(f"Iter = {iter}")
