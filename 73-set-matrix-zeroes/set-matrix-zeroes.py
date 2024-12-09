class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)      # Number of rows
        m = len(matrix[0])   # Number of columns
        row=set()
        col=set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(m):
                matrix[i][j]=0
        for i in range(n):
            for j in col:
                matrix[i][j]=0
        