class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findStartingIndex(nums, target):
            low, high = 0, len(nums) - 1
            start = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    start = mid
                    high = mid - 1  # move left to find the first occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return start
        
        def findEndingIndex(nums, target):
            low, high = 0, len(nums) - 1
            end = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    end = mid
                    low = mid + 1  # move right to find the last occurrence
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return end
        
        start = findStartingIndex(nums, target)
        if start == -1:
            return [-1, -1]  # target not found
        
        end = findEndingIndex(nums, target)
        return [start, end]

                
            
            