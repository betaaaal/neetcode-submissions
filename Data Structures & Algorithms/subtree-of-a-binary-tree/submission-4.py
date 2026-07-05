# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def preordertrav(self, root):
        res=[]
        def preorder(node):
            if not node:
                res.append('#')
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t1=self.preordertrav(root)
        t2=self.preordertrav(subRoot)
        for i in range(len(t1) - len(t2) + 1):
            if t1[i] == t2[0]:
                flag = True
                for j in range(len(t2)):
                    if t1[i + j] != t2[j]:
                        flag = False
                        break
                if flag:
                    return True

        return False
