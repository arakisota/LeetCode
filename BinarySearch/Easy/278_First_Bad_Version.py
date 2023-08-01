"""
時間計算量 : O(logn), 99.53%
空間計算量 : O(1), 34.38%
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left