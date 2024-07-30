# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root.left is None and root.right is None:
            return root.val == targetSum
        newTargetSum = targetSum - root.val
        
        left_has_path = self.hasPathSum(root.left, newTargetSum)
        right_has_path = self.hasPathSum(root.right, newTargetSum)
        
        return left_has_path or right_has_path