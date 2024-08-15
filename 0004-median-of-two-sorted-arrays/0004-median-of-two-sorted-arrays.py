class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine_list = nums1 + nums2
        sorted_list =  sorted(combine_list)
        
        length = len(sorted_list)
        
        if length % 2 == 1:
            median = sorted_list[length // 2]
            
        else:
            median = (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2.0
            
        return median    
            