class Solution(object):
    def maxArea(self, height):
        
        left, right = 0, len(height)-1
        
        maxArea = 0
        
        while(left < right):
            res = (right-left)*(min(height[left],height[right]))
            maxArea = max(maxArea,res)   
            if( height[right] > height[left]):
                left += 1
            else:
                right-=1
        return maxArea                   