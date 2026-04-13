class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summap = {}
        for i,v in enumerate(nums):
            if target-v in summap:
                return[summap[target-v],i]
            summap[v]=i

      
