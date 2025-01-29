class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, queens):
            for r , c in queens:
                if c == col or r-c == row-col or r+c == row + col:
                    return False 
            return True

        def backtrack (row, queens):
            if row == n:
                solution = []
                for r , c in queens:
                    line = '.' * c + 'Q' +'.' * (n-c-1)
                    solution.append(line)
                result.append(solution)
                return
            for col in range(n):
                if is_safe (row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1,queens)
                    queens.pop()
        result=[]
        backtrack(0,[])
        return result

                
        