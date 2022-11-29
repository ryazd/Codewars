# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start = 0
        end = 0
        max_l = 0
        uniq_char = set()
        while end < len(s):
            if s[end] not in uniq_char:
                uniq_char.add(s[end])
                end += 1
                max_l = max(max_l, len(uniq_char))
            else:
                uniq_char.remove(s[start])
                start += 1
        return max_l