"""
#242 from LeetCode

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

===============================================================================
===============================================================================
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # A1
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt

    # A2
        return sorted(list(s)) == sorted(list(t))

    # A3
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict1 == dict2