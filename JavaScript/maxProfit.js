var maxProfit = function(prices) {
    
    let max_profit = 0, day_price = prices[0];

    for (let i=0; i<prices.length; i++) {
        if (day_price > prices[i]) day_price = prices[i];

        if (prices[i] - day_price > max_profit) max_profit = prices[i] - day_price;
    }

    return max_profit;
};

console.log(maxProfit([7,1,5,3,6,4]));