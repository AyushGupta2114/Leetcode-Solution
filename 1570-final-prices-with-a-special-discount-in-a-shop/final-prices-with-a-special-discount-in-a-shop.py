class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        a = []
        
        for i in range(len(prices)):
            next_smaller = 0  # Start with the current number itself
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    next_smaller = prices[j]
                    break
            
            a.append(prices[i]-next_smaller)
        
        return a

        # a=[]
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)-1):
        #         if prices[i]>=prices[i] and j>i:
        #             discount=prices[j]
        #         a.append(prices[i]-discount)
        return a

        # if len(a)==0:
        #     return prices
        # if len(a)==len(prices)-2:
        #     a.append(prices[-2])
        #     a.append(prices[-1])
        #     return a


        