class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        n=len(arr)
        for i in range (n):
            for j in range(n):
                if arr[i] + arr[j]==target and i!=j:
                    return [i,j]
        return []