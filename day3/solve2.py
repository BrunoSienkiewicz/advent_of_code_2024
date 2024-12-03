import re
from collections import defaultdict

with open("input1.txt") as f:
    input = f.read()


dos_iter = re.finditer(r"do\(\)", input)
donts_iter = re.finditer(r"don\'t\(\)", input)

do = next(dos_iter).start()
dont = next(donts_iter).start()
prev_do = 0
prev_dont = -1

res = 0

# mul do dont -> mul.next
# mul dont do -> mul.next
# do mul dont -> mul.next, do.next
# dont mul do -> dont.next, mul.next
# do dont mul ->
# dont do mul

for m in re.finditer(r"mul\(\d+,\d+\)", input):
    mul = input[m.start() : m.end()]

    while dont < m.start():
        prev_dont = dont
        try:
            dont = next(donts_iter).start()
        except StopIteration:
            dont = 999998

    while do < m.start():
        prev_do = do
        try:
            do = next(donts_iter).start()
        except StopIteration:
            do = 999999

    print(f"do={prev_do}", f"dont={prev_dont}", f"start={m.start()}", res)
    if prev_dont < m.start() and prev_do < prev_dont:
        print("dont mul")
        continue
    n = mul.replace("mul(", "")
    n = n.replace(")", "")
    a, b = int(n.split(",")[0]), int(n.split(",")[1])
    res += a * b


print(res)
