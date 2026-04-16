class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        d = {}
        n = len(nums)
        for i in range(n):
            try:
                d[nums[i]]+=1
            except KeyError:
                d[nums[i]]=1
        # print(d)

        val= list(d.values())
        key = list(d.keys())
        for i in range(len(val)):
            if val[i] >= n/2:
                # print(key[i])
                return key[i]


