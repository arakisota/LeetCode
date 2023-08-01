"""
時間計算量 : O(logn), 21.53%
空間計算量 : O(n), 34.86%
"""

import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.append(10**8)
        ind = bisect.bisect_left(nums, target)
        if nums[ind] == target:
            return ind
        else:
            return -1