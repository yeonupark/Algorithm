class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        
        var ans = 0
        var min_val = prices[0]

        if prices.count == 1 {
            return 0
        }

        for i in 1...prices.count-1 {
            min_val = min(min_val, prices[i])
            ans = max(ans, prices[i] - min_val)
        }

        return ans
    }
}