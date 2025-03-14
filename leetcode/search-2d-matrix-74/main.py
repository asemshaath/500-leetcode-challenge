class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # (0,0) (2,3)
        # (2-0 // 2, 3-0 // 2) = (1, 1)
        # (1, 1) (2, 3)
        # (2+1 // 2, 1+3 // 2)
        # (1, 2)

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while r - l >= 0:
            m = (l + r) // 2
            m_element = matrix[m // len(matrix[0])][ m % len(matrix[0])]

            if m_element < target:
                l = m + 1
            elif m_element > target:
                r = m - 1
            else:
                return True
        return False
        
