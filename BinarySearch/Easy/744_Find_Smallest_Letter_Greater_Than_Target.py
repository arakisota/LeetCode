"""
時間計算量 : O(logn), 96.19%
空間計算量 : O(n), 29.81%
"""

from typing import List
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ind = bisect.bisect(letters, target) % len(letters)
        return letters[ind]