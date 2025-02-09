class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        NI = N - 1   #indexed 
 
        # reflect image vertically
        for row in matrix:
            l = 0
            r = N - 1

            while l <= r:
                temp = row[l]
                row[l] = row[r]
                row[r] = temp
                l += 1
                r -= 1
        # flip diognally 

        for i in range(N - 1):
            for j in range(N - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[NI - j][NI - i]
                matrix[NI - j][NI - i] = temp

    
            

        
