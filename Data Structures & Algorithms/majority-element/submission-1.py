class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res =0
        for i in range(len(nums)):
            if count ==0:
                count+=1
                res = nums[i]
            else:
                if nums[i]!= res:
                    count -=1
                else:
                    count+=1
        return res