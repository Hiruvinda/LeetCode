from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle list that will store the rows
        triangle = []

        # Loop through each row
        for row_num in range(numRows):
            # Start the row with a 1
            row = [1] * (row_num + 1)
            
            # Compute the values for the middle elements of the row
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
            # Append the completed row to the triangle
            triangle.append(row)
        
        return triangle

        