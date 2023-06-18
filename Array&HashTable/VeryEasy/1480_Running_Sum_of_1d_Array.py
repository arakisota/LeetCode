from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            ans.append(tmp_sum)

        return ans