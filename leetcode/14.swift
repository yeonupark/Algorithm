class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        
        var ans = ""

        for i in 0..<strs[0].count {
            let tmp = strs[0].prefix(i+1)
            for str in strs.dropFirst() {
                if str.prefix(i+1) != tmp {
                    return ans
                }
            }
            ans = String(tmp)
        }

        return ans
    }
}