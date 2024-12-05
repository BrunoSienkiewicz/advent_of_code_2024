from typing import DefaultDict


with open("test.txt", "r") as f:
    input = f.read().strip()

split_index = input.index("---")
lists = input[split_index + 3 :].strip().split("\n")
_graph = input[:split_index].strip().split("\n")

lists = [[int(el) for el in x.split(",")] for x in lists]


graph = DefaultDict(list)
for edge in _graph:
    u, v = edge.split("|")
    graph[int(u)].append(int(v))
    graph[int(v)]


def is_valid(l1: list[int], l2: list[int]):
    if len(l1) == 0:
        return True
    if len(l2) == 0:
        return True
    i, j = 0, 0

    while i < len(l1):
        if j == len(l2):
            break
        if l1[i] == l2[j]:
            j += 1
        i += 1
    return True if len(l2) == j else False


def dfs(n: int, l: list[int], path: list[int]):
    if not is_valid(l, path):
        return False
    if len(path) == len(l):
        return True
    if n in vis:
        return False

    vis.add(n)
    if n in l:
        path.append(n)
    print(path)
    res = False
    for nei in graph[n]:
        if dfs(nei, l, path):
            res = True
            break
    vis.remove(n)
    return res


res = []
for l in lists:
    vis = set()
    if dfs(l[0], l, []):
        res.append(l)
print(res)
res_sum = 0

for l in res:
    res_sum += l[len(l) // 2]
print(res_sum)
