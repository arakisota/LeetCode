from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = defaultdict(list)
        for ind, val in enumerate(nums):
            pair[val].append(ind)
        ans = 0
        for val in set(nums):
            length = len(pair[val])
            if length > 1:
                tmp = length * (length-1) // 2
                ans += tmp

        return ans