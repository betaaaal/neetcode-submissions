# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        curr=root

        while curr:
            if curr.left==None:
                result.append(curr.val)
                curr=curr.right

            else:
                leftChild=curr.left
                # find rightmost node in left subtree
                while leftChild.right!=None:
                    leftChild=leftChild.right
                # create thread
                leftChild.right=curr
                # move left and break original link
                temp=curr
                curr=curr.left
                temp.left=None
        return result
        
