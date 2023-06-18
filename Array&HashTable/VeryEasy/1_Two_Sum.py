from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(list)
        for ind, val in enumerate(nums):
            nums_dict[val].append(ind)

        for ind, val in enumerate(nums[:-1]):
            tmp = target - val
            if tmp in set(nums[:ind]+nums[ind+1:]):
                return [ind, nums_dict[tmp][-1]]