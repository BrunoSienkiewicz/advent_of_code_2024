print(sum([abs(sorted([int(l.split("   ")[0]) for l in open("input.txt").readlines()])[i] - sorted([int(l.split("   ")[1].replace("\n", "")) for l in open("input.txt").readlines()])[i]) for i in range(len(open("input.txt").readlines()))]))
