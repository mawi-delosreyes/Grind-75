def removeElement(nums: list[int], val: int) -> int:
    nums[:] = [x for x in nums if x != val]
    return len(nums)


print(removeElement([3,2,2,3], 3))