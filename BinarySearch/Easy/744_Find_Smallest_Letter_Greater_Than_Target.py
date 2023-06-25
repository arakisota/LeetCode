from typing import List
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[bisect.bisect(letters, target) % len(letters)]
        return ans