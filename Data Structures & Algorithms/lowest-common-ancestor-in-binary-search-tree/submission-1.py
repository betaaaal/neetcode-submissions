# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getpath(self, root, target):
        path=[]
        while root:
            path.append(root)
            if root.val==target.val:
                return path
            elif target.val<root.val:
                root=root.left
            else:
                root=root.right
        return []
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pathP=self.getpath(root, p)
        pathQ=self.getpath(root, q)

        lca=None
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i]==pathQ[i]:
                lca=pathP[i]
            else:
                break
        return lca
