# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)       # Traverse left subtree
            result.append(node.val)  # Visit root node
            inorder(node.right)      # Traverse right subtree
        
        inorder(root)
        return result