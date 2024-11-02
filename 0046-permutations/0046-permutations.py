from itertools import permutations
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = [list(perm) for perm in permutations(nums)]
        return all_permutations