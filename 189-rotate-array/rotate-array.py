class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            k %= len(nums)

            temp=[]
            for i in range(len(nums)-k,len(nums)):
                temp.append(nums[i])
            for i in range(len(nums)-k- 1, -1, -1):
                nums[i+k]=nums[i]
            for i in range(k):
                nums[i]=temp[i]


        
        