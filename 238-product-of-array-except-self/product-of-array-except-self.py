class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        leftproduct=1
        for i in range(len(nums)):
            res[i]=leftproduct
            leftproduct *=nums[i]
        rightproduct=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=rightproduct
            rightproduct*=nums[j]
        return res