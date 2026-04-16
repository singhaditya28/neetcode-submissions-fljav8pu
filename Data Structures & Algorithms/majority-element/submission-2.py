class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 0
        d = {}
        n = len(nums)
        res = 0
        for i in range(n):
            d[nums[i]]=1 + d.get(nums[i],0)
            res = nums[i] if d[nums[i]]>maxCount else res
            maxCount = max(d[nums[i]],maxCount)
        return res


