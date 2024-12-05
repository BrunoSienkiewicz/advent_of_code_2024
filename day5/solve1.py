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


def dfs(n: int, l: list[int], path: list[int]):
    if n in vis:  # check for cycle
        return False

    vis.add(n)
    if n in l:
        path.append(n)

    if l == path:  # found proper order
        return True
    if l[: len(path)] != path:  # order is violated
        vis.remove(n)
        if n in l:
            path.pop()
        return False

    res = False
    for nei in graph[n]:
        if dfs(nei, l, path):
            res = True
            break
    vis.remove(n)
    if n in l:
        path.pop()
    return res


res = []
_total = len(lists)
_progress = 0
for l in lists:
    print(f"{_progress}/{_total}")
    vis = set()
    if dfs(l[0], l, []):
        res.append(l)
    _progress += 1
print(res)
res_sum = 0

for l in res:
    res_sum += l[len(l) // 2]
print(res_sum)
