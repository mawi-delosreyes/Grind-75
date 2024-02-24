var twoSum = function(nums, target) {
    const num = new Map();

    for (let i=0; i<nums.length; i++) {
        if (num.size > 0){
            let x = target - nums[i];
            if (num.has(x)) {
                return [num.get(x), i];
            } 
        }
        num.set(nums[i], i);
    }
};


console.log(twoSum([2,7,11,15], 9));
