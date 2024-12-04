with open("input.txt", "r") as f:
    lines = f.readlines()
grid = [list(l.replace("\n", "")) for l in lines]
vis = set()


def dfs(r, c, cur_word, dir):
    if cur_word == "XMAS":
        return 1
    if c < 0 or r < 0 or r == len(grid) or c == len(grid[0]):  # or (r, c) in vis:
        return 0
    if len(cur_word) == 4:
        return 0

    return dfs(r + dir[0], c + dir[1], cur_word + grid[r][c], dir)


res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        for dir in [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1],
            [-1, 1],
            [1, -1],
            [-1, -1],
            [1, 1],
        ]:
            res += dfs(i, j, "", dir)
print(res)
