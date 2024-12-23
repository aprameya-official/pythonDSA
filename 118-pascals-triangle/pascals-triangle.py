class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        def generateRow(row):
            ans = 1
            ansRow = [1] #inserting the 1st element
            
            #calculate the rest of the elements:
            for col in range(1, row):
                ans *= (row - col)
                ans //= col
                ansRow.append(ans)
            return ansRow
        ans = []
        for row in range(1, n+1):
            ans.append(generateRow(row))
        return ans        