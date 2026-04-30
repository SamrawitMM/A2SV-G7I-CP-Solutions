# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        def deleteNode(root, key):
            
            if root:

                if root.val > key:
                    root.left = deleteNode(root.left, key)
                
                elif root.val < key:
                    root.right = deleteNode(root.right, key)


                else:

                    if root.left is None and  root.right is None:
                        return None

                    if root.left is None:
                        return root.right
                    
                    elif root.right is None:
                        return root.left

                
                    curr = root.right

                    while curr.left:
                        curr = curr.left

                    
                    root.val = curr.val
                    root.right = deleteNode(root.right, curr.val)

                return root

        
        return deleteNode(root, key)





            

        # def search(root, key):

        #     if root:

        #         if root.val > key:
        #             search(root.left, key)

        #         if root.val == key:
        #             root.right


