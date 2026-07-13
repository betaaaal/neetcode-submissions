"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def isAllSame(self, grid, x,y,n):
        val=grid[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if grid[i][j]!=val:
                    return False
                    break
        return True
    def solve(self, grid, x,y,n):
        if self.isAllSame(grid, x, y, n):
            return Node(grid[x][y], True, None, None, None, None)
        half=n//2
        topLeft=self.solve(grid, x,y,half)
        topRight=self.solve(grid, x, y+half, half)
        bottomLeft=self.solve(grid, x+half,y,half)
        bottomRight=self.solve(grid, x+half, y+half, half)
        return Node(
            False,
            False,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
        )
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.solve(grid, 0,0, len(grid))