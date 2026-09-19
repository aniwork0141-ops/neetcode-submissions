class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = float('inf') #positive infinity
        for p in prices:
            mn = min(mn,p) #min so far => buy at
            mx = max(mx, p - mn) #profit if sold today
        return mx