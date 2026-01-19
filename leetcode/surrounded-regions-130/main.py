class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        (1,1), (1,2), (2,2)
        
        """

        region = set()
        R = len(board)
        C = len(board[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def get_region(x, y):
            q = deque([(x,y)])
            region.add((x,y))

            while q:
                ix, iy = q.popleft()

                for dx, dy in directions:
                    ax = dx + ix
                    ay = dy + iy

                    if ax >= 0 and ay >= 0 and ax < R and ay < C and (ax, ay) not in region:
                        if board[ax][ay] == 'O':
                            q.append((ax, ay))
                            region.add((ax, ay))
                    


        def capture():
            must_capture = True

            for x, y in region:
                if not must_capture:
                    break
                for dx, dy in directions:
                    ax = x + dx
                    ay = y + dy

                    if ax >= 0 and ay >= 0 and ax < R and ay < C: 
                        
                        # and (ax, ay) in region:
                        continue
                    else:
                        must_capture = False
                        break
            
            if must_capture:
                for x, y in region:
                    board[x][y] = 'X'


            
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    region = set()
                    get_region(r, c)
                    capture()






