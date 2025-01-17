"""
Solution for the problem "217. Contains Duplicate"
Not the most efficient solution but it works.

Time complexity: O(n^2)
Space complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True
        
        return False
"""

"""
Time complexity: O(nlogn)
Space complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

"""

# Use set to store the elements and check if the element is already in the set.
# If it is, return True. Otherwise, add the element to the set.
# If the loop ends, return False.
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        set1 = set()

        for x in nums:
            if x in set1:
                return True
            set1.add(x)
        return False