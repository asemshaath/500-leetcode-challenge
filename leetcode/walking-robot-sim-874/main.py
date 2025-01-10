class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr = (0, 0)
        direction = (0, 1)  # north
        distance = 0
        obs = {tuple(o) for o in obstacles}

        for cmd in commands:
            if cmd == -1:
                x, y = direction
                direction = (y, -x)
            elif cmd == -2:
                x, y = direction
                direction = (-y, x)
            else:
                cx, cy = curr
                x, y = direction

                # cx = cx + x * cmd
                # cy = cy + y * cmd
                
                # curr = (cx, cy)

                # distance = max(distance, cx**2 + cy**2)

                for _ in range(cmd):
                    cx = cx + x
                    cy = cy + y
                    if (cx, cy) in obs:
                        break
                    curr = (cx, cy)
                    distance = max(distance, cx**2 + cy**2)



        return distance
