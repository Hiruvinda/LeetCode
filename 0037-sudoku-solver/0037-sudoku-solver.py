from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num:
                    return False

            for i in range(9):
                if board[i][col] == num:
                    return False

            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[box_row + i][box_col + j] == num:
                        return False
            return True

        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num

                                if backtrack(board):
                                    return True

                                board[row][col] = '.'
                        return False
            return True

        backtrack(board)
