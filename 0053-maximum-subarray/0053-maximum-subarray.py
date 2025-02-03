from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables for Kadane's algorithm
        current_sum = max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Either extend the current subarray or start a new one
            current_sum = max(num, current_sum + num)
            # Update the maximum sum if needed
            max_sum = max(max_sum, current_sum)
        
        return max_sum
