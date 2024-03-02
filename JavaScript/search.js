var search = function(nums, target) {
    
    let low = 0, high = nums.length-1, mid;

    while (low <= high) {
        mid = low + Math.floor((high-low)/2);
        if (target == nums[mid]) {
            return mid;
        } 

        if (target > nums[mid]) {
            low = mid + 1;
        }
        if (target < nums[mid]) {
            high = mid - 1;
        }
    }
    return -1;
};

console.log(search([-1,0,3,5,9,12], 9))