class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                row_key=(board[i][j],"row",i)
                col_key=(board[i][j],"col",j)
                box_key=(board[i][j],"box",i//3,j//3)
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True
                