class Solution:
    def rotate(self, matrix: List[List[int]]):
        n = len(matrix)
        rotated =[row[:] for row in matrix]  
        for i in range(n):
            for j in range(n):
                matrix[j][n - i - 1] = rotated[i][j]
 

        