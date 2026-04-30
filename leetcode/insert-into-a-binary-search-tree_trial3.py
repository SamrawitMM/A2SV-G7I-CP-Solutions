# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new_node = TreeNode(val)
            return new_node


        def search(root, val):
            
            if root:
                if root.val < val:
                    search(root.right, val)
                    if not root.right:
                        new_node = TreeNode(val)
                        root.right = new_node
                        return 
                    

                elif root.val > val:
                    search(root.left, val)
                    if not root.left:
                        new_node = TreeNode(val)
                        root.left = new_node
                        return

        search(root, val)
        return root
        