"""
時間計算量 : O(n), 99.53%
空間計算量 : O(1), 85.6%
"""

from typing import List
from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


"""class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            ans.append(tmp_sum)

        return ans"""