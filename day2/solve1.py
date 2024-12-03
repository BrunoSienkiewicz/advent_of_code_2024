def is_safe(line):
    nums = [int(n) for n in line.split(" ")]

    inc = 3 if nums[0] < nums[1] else -3

    if nums[0] < nums[1]:
        for i in range(1, len(nums)):
            if nums[i - 1] + inc < nums[i] or nums[i - 1] - nums[i] == 0:
                return False
    elif nums[0] > nums[1]:
        for i in range(1, len(nums)):
            if nums[i - 1] + inc > nums[i] or nums[i - 1] - nums[i] == 0:
                return False
    else:
        return False

    return True


with open("input.txt") as f:
    lines = f.readlines()

res = 0
for l in lines:
    if is_safe(l):
        res += 1
        print(l)

print(res)
