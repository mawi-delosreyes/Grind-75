
class Solution {
    public int search(int[] nums, int target) {
        
        int low = 0, high = nums.length, mid, cur;

        if (nums[0] > target || nums[nums.length-1] < target) { 
            return -1;
        }

        while (low <= high) {
            mid = low + (high-low)/2;
            cur = nums[mid];

            if (target > cur) {
                low = mid + 1;
            } else if (target < cur) {
                high = mid - 1;
            } else { return mid; }

        }
        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        int[] nums = {-1,0,3,5,9,12};
        int target = 9;
        Solution solution = new Solution();
        System.out.print(solution.search(nums, target));
    }
}