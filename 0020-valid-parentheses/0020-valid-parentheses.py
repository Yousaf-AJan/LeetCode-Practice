class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 is not 0:
            return False

        stack = []
        b_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in b_map:
                top = stack.pop() if stack else '?'
                if top != b_map[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack



        