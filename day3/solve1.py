import re

with open("input1.txt") as f:
    input = f.read()

res = 0

for m in re.finditer(r"mul\(\d+,\d+\)", input):
    m = input[m.start() : m.end()]
    print(m)

    n = m.replace("mul(", "")
    n = n.replace(")", "")
    a, b = int(n.split(",")[0]), int(n.split(",")[1])
    print(m, a, b)
    res += a * b

print(res)
