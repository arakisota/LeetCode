"""
時間計算量 : O(nlogn+mn), 70.20%
空間計算量 : O(n), 66.15%
PythonのsortはTimSortだから、sortするときにO(n)の追加の配列が必要になる。C++やJAVAだとQuickSortやHeapSortになるからO(logn)になる。
"""

import bisect
from itertools import accumulate
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        sum_nums = list(accumulate(nums))
        for q in queries:
            ind = bisect.bisect_right(sum_nums, q)
            ans.append(ind)

        return ans