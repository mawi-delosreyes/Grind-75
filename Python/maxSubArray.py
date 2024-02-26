def maxSubArray(nums: list[int]) -> int:

    max_sum = float('-inf')
    total = 0

    for i in nums:
        total += i
        max_sum = max(max_sum, total)
        if total < 0: total = 0

    return max_sum





print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))