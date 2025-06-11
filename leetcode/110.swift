/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func isBalanced(_ root: TreeNode?) -> Bool {

        guard let root else {
            return true
        }

        return getHeight(root) == nil ? false : true
    }

    func getHeight(_ root: TreeNode?) -> Int? {

        guard let root else {
            return 0
        }

        guard let leftHeight = getHeight(root.left) else {
            return nil
        }
        guard let rightHeight = getHeight(root.right) else {
            return nil
        }

        if abs(leftHeight - rightHeight) > 1 {
            return nil
        }

        return max(leftHeight, rightHeight) + 1
    }
}