class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_str = str(x)

        index = 0
        
        for i in reversed(x_str):
            if i != x_str[index]:
                return False
            index+=1

        return True 

        