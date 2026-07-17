# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, preorder, inorder, start, end, idx):
        if start>end:
            return None
        
        root_val= preorder[idx[0]]
        i=start

        while i<=end:
            if inorder[i]==root_val:
                break
            i+=1
        idx[0]+=1

        root=TreeNode(root_val)
        root.left=self.solve(preorder, inorder,start , i-1, idx)
        root.right=self.solve(preorder, inorder, i+1, end, idx)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx=[0]

        return self.solve(preorder, inorder,0, len(preorder)-1, idx)
        #It's simply a list of length 1 used as a workaround to mimic C++'s pass-by-reference behavior.