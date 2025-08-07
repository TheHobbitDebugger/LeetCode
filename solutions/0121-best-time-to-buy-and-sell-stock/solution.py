class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = (0)
        min = float(10**5)

        for i in prices:
            if i < min:
                min = i
        
            profit = i - min

            if profit > max:
                max = profit

        return max  

#O(n)
#O(1)
