from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrange_s = Counter(s)
        arrange_t = Counter(t)
        if arrange_s == arrange_t:
            return True
        else:
            return False