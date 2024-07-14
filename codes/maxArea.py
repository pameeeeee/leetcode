class Solution: #max area
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        baskom=0
    
        while l<r:
            baskom_temp=min(height[l],height[r])*(r-l)
            baskom=max(baskom,baskom_temp)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return baskom