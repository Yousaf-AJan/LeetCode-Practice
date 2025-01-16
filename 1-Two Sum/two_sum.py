class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Dict = {}

        for i in range(len(nums)):
            sub = target - nums[i]

            if sub in Dict:
                return [i, Dict[sub]]
            Dict[nums[i]]=i

        return [] 