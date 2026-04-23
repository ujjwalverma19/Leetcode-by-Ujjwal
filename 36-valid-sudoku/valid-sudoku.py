class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                box_key = (i // 3, j // 3)
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes.get(box_key, set())):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                if box_key not in boxes:
                    boxes[box_key] = set()
                boxes[box_key].add(num)
        return True