def removeDuplicates(nums: list[int]) -> int:
    s = set(nums)
    nums.clear()
    for i in s:
        nums.append(i)
    nums.sort()

    return len(nums)



print(removeDuplicates([-1,0,0,0,0,3,3]))