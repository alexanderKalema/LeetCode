class Solution(object):
    def climbStairs(self, n):
        prev, nex = 1, 1
        res = 1
        for int in range(n,1,-1):
            res = prev + nex
            nex = prev
            prev = res
        return res    
            
        