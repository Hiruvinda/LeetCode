class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
           
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            
            for num in counter:
                if counter[num] > 0:
                   
                    path.append(num)
                    counter[num] -= 1
                    
                  
                    backtrack(path, counter)
                    
                
                    path.pop()
                    counter[num] += 1

        from collections import Counter
        result = []
        counter = Counter(nums) 
        backtrack([], counter)
        return result

        