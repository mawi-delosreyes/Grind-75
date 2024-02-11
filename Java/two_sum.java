import java.util.HashMap;

class Solution {
    int[] twoSum(int[] nums, int target) {

        HashMap <Integer, Integer> maps = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (maps.containsKey(diff)) {
                return new int[] {maps.get(diff), i};
            }
            maps.put(nums[i], i);
        }
        return new int[] {};
    }
}

class Main {
    public static void main(String[] args) {
        int[] nums = {3,2,3};
        int target = 6;
        Solution solution = new Solution();
        System.out.print(solution.twoSum(nums, target));
    }
}