class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        if nums[0] > target or nums[-1] < target: return -1

        while low <= high:
            mid = int(low + (high-low)/2)

            if nums[mid] == target: return mid
            else:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


        