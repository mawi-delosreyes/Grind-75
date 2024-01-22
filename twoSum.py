class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_list = []

        for _i in range(len(nums)):
            _diff = target - nums[_i]
            if _diff in nums and nums.index(_diff) != _i:
                sum_list.append(_i)
                sum_list.append(nums.index(_diff))
                break
        return sum_list

            
        