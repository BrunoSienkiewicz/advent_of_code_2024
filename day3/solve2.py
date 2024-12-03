import re
from collections import defaultdict

with open("input1.txt") as f:
    input = f.read()

do = [0] + [d.start() for d in re.finditer(r"do\(\)", input)] + [len(input)]
dont = [-1] + [d.start() for d in re.finditer(r"don\'t\(\)", input)] + [len(input)]
do_ptr = 1
dont_ptr = 1

res = 0

# mul do dont -> mul.next
# mul dont do -> mul.next
# do mul dont -> mul.next, do.next
# dont mul do -> dont.next, mul.next
# do dont mul ->
# dont do mul

for m in re.finditer(r"mul\(\d+,\d+\)", input):
    mul = input[m.start() : m.end()]

    if dont_ptr < len(dont):
        while dont[dont_ptr] < m.start():
            dont_ptr += 1

    if do_ptr < len(do):
        while do[do_ptr] < m.start():
            do_ptr += 1

    print(f"do={do[do_ptr-1]}", f"dont={dont[dont_ptr-1]}", f"start={m.start()}", res)
    if dont[dont_ptr - 1] < m.start() and do[do_ptr - 1] < dont[dont_ptr - 1]:
        print("dont mul")
        continue
    n = mul.replace("mul(", "")
    n = n.replace(")", "")
    a, b = int(n.split(",")[0]), int(n.split(",")[1])
    res += a * b


print(res)
