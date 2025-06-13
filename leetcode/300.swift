class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var dp = Array(repeating: 1, count: nums.count)
        var max_val = nums[0]
        var max_idx = 0

        func makeTable(_ i: Int) {
            if i == 0 {
                return
            }

            if nums[i] > max_val {
                dp[i] = dp[max_idx] + 1
                max_val = nums[i]
                max_idx = i
            } else {
                var j = i-1
                var tmp = 1
                while(j > -1) {
                    if nums[j] < nums[i] {
                        tmp = max(tmp, dp[j]+1)
                    }
                    j -= 1
                }
                dp[i] = tmp
                if dp[i] > dp[max_idx] {
                    max_val = nums[i]
                    max_idx = i
                }
            }
        }

        for i in 0..<nums.count {
            makeTable(i)
        }
        return dp.max() ?? 1
    }
}