class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(0,len(prices)):
            for j in range(0,i):
                if(prices[i]+prices[j]<=money):
                    print(prices[i],prices[j])
                    return money-(prices[i]+prices[j])
        return money


        