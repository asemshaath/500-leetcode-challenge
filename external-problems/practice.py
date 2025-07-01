"""
Right here I will have all the dirt aka behind the scenes of me either solving problems or practicing for interviews.
This is just a file to fill my github commit dashboard in green and flex on other developers.
"""
from typing import List


def predictAnswer(stockData: List[int], queries: List[int]) -> List[int]:
    res = []
    for q in queries:
        nearest = (float('inf'), q + 1)
        for i in range(len(stockData)):
            val, dis = nearest
            real_i = i + 1
            if val > stockData[q - 1] and abs(real_i - q) < dis:
                print('cond satisfied')
                nearest = (stockData[i], abs(real_i - q))

        v, d = nearest
        if v == float('inf'):
            res.append(-1)
        else:
            res.append(d)

    return res
    
if __name__ == "__main__":
    stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    queries = [6, 5, 4]
    res = predictAnswer(stockData, queries)
    #expected output: [5,4,8]

    print(res)  


