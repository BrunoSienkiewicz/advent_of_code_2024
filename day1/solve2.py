from typing import Counter

score = 0

d1 = [int(l.split("   ")[0]) for l in open("input2.txt").readlines()]
d2 = [int(l.split("   ")[1].replace("\n", "")) for l in open("input2.txt").readlines()]
l2 = Counter()

for d in d2:
    l2[d]+=1

for d in set(d1):
    score += d*l2[d]

print(score)

