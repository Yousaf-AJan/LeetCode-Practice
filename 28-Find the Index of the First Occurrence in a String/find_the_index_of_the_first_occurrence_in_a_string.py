"""
Same solution written in another way. For some reason doesn't pass leetcode testcases

for i in range(len(haystack) - len(needle) + 1):
    for j in range(len(needle)):
        if haystack[i+j] != needle[j]
            break
        if j == len(needle) - 1:
            return i

return -1

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
