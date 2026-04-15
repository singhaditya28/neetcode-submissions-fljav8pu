class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k= len(nums)
        for i in range(len(nums)):
            if nums[i]==val:
                # nums.append(nums.pop(i))
                nums[i]=51
                k-=1
                
        nums.sort()
        print(k,nums)
        return k