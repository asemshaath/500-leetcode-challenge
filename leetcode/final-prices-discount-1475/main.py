class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []

        for i in range(len(prices)):
            discount = 20000
            for j in range(i+1, len(prices)):
                # discount = min(prices[j], discount)
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            
            if discount <= prices[i]:
                t = prices[i] - discount
                answer.append(t)
            else:
                answer.append(prices[i])

        return answer
