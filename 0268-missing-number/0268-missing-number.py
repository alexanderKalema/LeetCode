class Solution(object):
    def missingNumber(self, nums):
        
        totalSum = (len(nums)/2.0)*(1+len(nums))
        
        for item in nums:
            totalSum = totalSum - item
            
        return int(totalSum)    