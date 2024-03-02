def searchInsert(nums: list[int], target: int) -> int:

    if target > nums[-1]: return len(nums)
    if target < nums[0]: return 0

    if target in nums: return nums.index(target)
    else:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2

            if target > nums[mid]:
                if target < nums[mid+1]: return mid+1
                low = mid + 1
            elif target < nums[mid]:
                if target > nums[mid-1]: return mid
                high = mid - 1        
        return low




print(searchInsert([1,3, 5, 6], 4))
