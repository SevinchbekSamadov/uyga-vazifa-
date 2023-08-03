class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        s = 0
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if prices[j] - prices[i] > s:
                    s = prices[j] - prices[i]
        return s
            
a = Solution()
print(a.maxProfit(prices = [7,1,5,3,6,4]))
#5
print(a.maxProfit(prices = [7,6,4,3,1]))
#0