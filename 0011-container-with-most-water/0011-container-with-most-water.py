class Solution:
    def maxArea(Self,height: list[int]) -> int:
    
        left, right = 0, len(height) - 1
        max_water = 0
    
    
        while left < right:
        
            width = right - left
        
        
            current_height = min(height[left], height[right])
        
        
            current_water = width * current_height
        
        
            max_water = max(max_water, current_water)
        
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_water