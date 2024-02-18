def majorityElement(nums: list[int]) -> int:
    size = len(nums)
    holder = {}
    for i in nums:
        if i in holder: holder[i] += 1
        else: holder[i] = 1

        if holder[i] > size/2:
            return i
        
print(majorityElement([3,2,3]))