var climbStairs = function(n) {
  
    let last_num = 0, n_steps = 1;

    for (let i=0; i<n; i++) {
        n_steps += last_num;
        last_num = n_steps - last_num;
    }

    return n_steps;
    
};

console.log(climbStairs(5));