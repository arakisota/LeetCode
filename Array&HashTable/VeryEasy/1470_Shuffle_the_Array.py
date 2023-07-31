"""
時間計算量 : O(n), 99.87%
空間計算量 : O(n), 38.50%
"""

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans