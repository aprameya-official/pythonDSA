class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        temp=arr.copy()
        arr.sort()
        start = 0
        end = len(arr) - 1
        while start < end:
            currsum = arr[start] + arr[end]
            if currsum == target:
                ans=[]
                for i in range(len(temp)):
                    if arr[start]==temp[i] or arr[end]==temp[i]:
                        ans.append(i)

                return ans
            if currsum > target:
                end -= 1
            else:
                start += 1
        return -1