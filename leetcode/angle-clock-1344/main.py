class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_pos = 0 if minutes == 0 else (minutes / 60) * 360
        hour_pos = ((minutes / 60) * 30) if hour == 12 else (hour * 30) + ((minutes / 60) * 30)
        res = 0
        if hour_pos <= min_pos:
            res = min_pos - hour_pos
        else:
            res = hour_pos - min_pos

        if res > 180:
            res = 360 - res
        return res

