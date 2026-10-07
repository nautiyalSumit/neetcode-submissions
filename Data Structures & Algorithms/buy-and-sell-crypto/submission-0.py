class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        res=0
        while right<len(prices):
            res=max(res,prices[right]-prices[left])
            if prices[left]>prices[right]:
                left=right
            right+=1
        return res