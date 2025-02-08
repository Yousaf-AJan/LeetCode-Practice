from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""
        
        strs.sort()
        
        first, last = strs[0], strs[-1]
        common_prefix = []
        
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
        
        return "".join(common_prefix)
