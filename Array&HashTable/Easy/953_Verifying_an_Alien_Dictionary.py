from typing import List
from string import ascii_lowercase

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_words = []
        alphabet = ascii_lowercase
        for word in words:
            tmp = str()
            for s in word:
                ind = order.index(s)
                tmp += alphabet[ind]
            alien_words.append(tmp)

        sorted_alien_words = sorted(alien_words)
        if sorted_alien_words == alien_words:
            return True
        else:
            return False