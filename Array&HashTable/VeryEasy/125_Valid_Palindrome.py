"""
時間計算量 : O(n), 87.29%
空間計算量 : O(n), 74.28%
"""

#from string import ascii_lowercase

class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = str()
        for feature in s.lower().replace(" ", ""):
            if feature.isalnum():
                palindrome += feature
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False

"""class Solution:
    def isPalindrome(self, s: str) -> bool:
        num = set([str(i) for i in range(10)])
        num = num | set(ascii_lowercase)
        new_s = s.lower()
        for feature in list(new_s):
            if feature not in num:
                new_s = new_s.replace(feature, "")
        if new_s == new_s[::-1]:
            return True
        else:
            return False"""