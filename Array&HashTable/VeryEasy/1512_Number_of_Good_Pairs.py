"""
時間計算量 : O(1), 91.58%
空間計算量 : O(n), 92.62%
"""

from typing import List
from collections import Counter
#from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def combinations(n):
            return n * (n-1) // 2
        count = Counter(nums)
        answer = 0
        for cnt in count.values():
            if cnt > 1:
                answer += combinations(cnt)
        return answer

"""
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
"""