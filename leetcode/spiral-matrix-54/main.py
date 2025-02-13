class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        check the validity of the element of the current direction (if not valid or vistied change direction)
        do until you visit all the nodes
        """
        visit = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0) ] # right - down - left - up
        curr_dir = 0
        curr = (0, 0)
        L_MAT = len(matrix) * len(matrix[0])
        res = []

        while len(visit) < L_MAT:
            cx, cy = curr
            dx, dy = directions[curr_dir]
            

            if cx >= 0 and cx < len(matrix) and cy >= 0 and cy < len(matrix[0]): 
                res.append(matrix[cx][cy])
                visit.add((cx, cy))

                if cx + dx >= len(matrix) or cx + dx < 0 or cy + dy >= len(matrix[0]) or cy + dy < 0 or (cx + dx, cy + dy) in visit:
                    #  change direction
                    curr_dir = curr_dir + 1 if curr_dir < 3 else 0
                # else:
                dx, dy = directions[curr_dir]
                curr = (cx + dx, cy + dy)

        return res


