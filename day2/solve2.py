def check_nums(nums):
    inc = 3 if nums[0] < nums[1] else -3
    if nums[0] < nums[1]:
        for i in range(1, len(nums)):
            if nums[i - 1] + inc < nums[i]:
                return False
            if nums[i - 1] - nums[i] == 0:
                return False
            if nums[i - 1] > nums[i]:
                return False
    elif nums[0] > nums[1]:
        for i in range(1, len(nums)):
            if nums[i - 1] + inc > nums[i]:
                return False
            if nums[i - 1] - nums[i] == 0:
                return False
            if nums[i - 1] < nums[i]:
                return False
    else:
        return False
    return True


def is_safe(line):
    nums = [int(n) for n in line.split(" ")]

    if check_nums(nums):
        return True

    for i in range(0, len(nums)):
        _nums = nums.copy()
        _nums.pop(i)
        if check_nums(_nums):
            return True

    return False


with open("input.txt") as f:
    lines = f.readlines()

res = 0
for l in lines:
    if is_safe(l):
        print(l)
        res += 1

print(res)
