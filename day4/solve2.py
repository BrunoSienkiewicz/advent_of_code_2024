with open("test.txt", "r") as f:
    lines = f.readlines()
grid = [list(l.replace("\n", "")) for l in lines]
vis = set()


def check(r, c):
    res = 0
    if (grid[r - 1][c - 1] == "M" and grid[r + 1][c + 1] == "S") or (
        grid[r - 1][c - 1] == "S" and grid[r + 1][c + 1] == "M"
    ):
        res += 1
    if (grid[r + 1][c - 1] == "M" and grid[r - 1][c + 1] == "S") or (
        grid[r + 1][c - 1] == "S" and grid[r - 1][c + 1] == "M"
    ):
        res += 1
    if res == 2:
        return 1
    else:
        return 0


res = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == "A":
            res += check(i, j)
print(res)
