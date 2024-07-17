class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize the pointers for nums1 and nums2 respectively.
        p1 = m - 1
        p2 = n - 1
        # Initialize the pointer for the end of nums1 array
        p = m + n - 1
        
        # While there are elements to be compared in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
        