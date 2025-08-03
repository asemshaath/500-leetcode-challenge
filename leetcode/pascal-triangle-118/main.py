class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1], [1,1]]

        if numRows < 3:
            return pascal_triangle[:numRows]

        for i in range(3, numRows+1):
            bottom = pascal_triangle[-1]
            new_bottom = [1]
            p1, p2 = 0, 1
            while p2 < i-1:
                new_bottom.append(bottom[p1] + bottom[p2])
                p1 += 1
                p2 += 1
            new_bottom.append(1)
            pascal_triangle.append(new_bottom)

        return pascal_triangle
