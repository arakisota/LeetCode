from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = Counter(words[0])
        for word in words[1:]:
            ans &= Counter(word)

        return list(ans.elements())