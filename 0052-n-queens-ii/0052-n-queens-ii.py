class Solution:
    def totalNQueens(self, n: int) -> int:
        # To count the number of solutions
        self.count = 0

        # Helper function to check if the position is valid
        def is_valid(row, col, columns, diag1, diag2):
            return col not in columns and (row - col) not in diag1 and (row + col) not in diag2

        # Backtracking function
        def backtrack(row, columns, diag1, diag2):
            # If all queens are placed, increment the solution count
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if is_valid(row, col, columns, diag1, diag2):
                    # Place the queen and mark attacking paths
                    columns.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)

                    # Recurse to the next row
                    backtrack(row + 1, columns, diag1, diag2)

                    # Remove the queen and backtrack
                    columns.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)

        # Start the backtracking process
        backtrack(0, set(), set(), set())

        return self.count