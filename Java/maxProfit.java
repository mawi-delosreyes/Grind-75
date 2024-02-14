
class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0, min_day = prices[0];

        for (int x : prices) {
            if (x < min_day) { min_day = x; }
            
            if (max_profit < (x - min_day)) {
                max_profit = x - min_day; 
            }
        }
        return max_profit;
    }
}

class Main {
    public static void main(String[] args) {
        int[] prices = {7,6,4,3,1};
        Solution solution = new Solution();
        System.out.print(solution.maxProfit(prices));
    }
}