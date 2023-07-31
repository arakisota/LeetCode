"""
時間計算量 : O(n), 67.52%
空間計算量 : O(n), 92.7%
"""

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans