import re

with open("input1.txt") as f:
    input = f.read()


dos_iter = re.finditer(r"do\(\)", input)
donts_iter = re.finditer(r"don\'t\(\)", input)

do = next(dos_iter).start()
dont = next(donts_iter).start()

res = 0

# mul do dont -> mul.next
# mul dont do -> mul.next
# do mul dont -> mul.next, do.next
# dont mul do -> dont.next, mul.next
# do dont mul ->
# dont do mul

for m in re.finditer(r"mul\(\d+,\d+\)", input):
    mul = input[m.start() : m.end()]
    print(mul, do, dont, m.start(), res)

    while dont < m.start():
        try:
            dont = next(donts_iter).start()
        except StopIteration:
            dont = 999998

    while do < m.start():
        try:
            do = next(donts_iter).start()
        except StopIteration:
            do = 999999

    if do > dont:
        n = mul.replace("mul(", "")
        n = n.replace(")", "")
        a, b = int(n.split(",")[0]), int(n.split(",")[1])
        res += a * b
        continue
    if do < dont:
        continue


print(res)
