class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxheight = 0
        while j>i:
            maxheight = max((j-i)*min(heights[i],heights[j]),maxheight)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxheight