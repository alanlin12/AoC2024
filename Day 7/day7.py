def calc_sums(nums, target) -> bool:
    if len(nums) == 1: return target == nums[0]
    if target % nums[-1] == 0 and calc_sums(nums[:-1], target // nums[-1]): return True
    if target > nums[-1] and calc_sums(nums[:-1], target - nums[-1]): return True
    if len(str(target)) > len(str(nums[-1])) and str(target).endswith(str(nums[-1])) and calc_sums(nums[:-1], int(str(target)[:-len(str(nums[-1]))])): return True
    return False


with open("input.txt", "r") as file:
    ans = 0
    for line in file:
        l, r = line.split(": ")
        target = int(l)
        nums = [int(x) for x in r.split()]
        if calc_sums(nums, target):
            ans += target

    print(ans)