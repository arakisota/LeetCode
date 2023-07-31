"""
時間計算量 : O(1), 98.94%
空間計算量 : O(n), 99.26%
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrange_s = Counter(s)
        arrange_t = Counter(t)
        if arrange_s == arrange_t:
            return True
        else:
            return False