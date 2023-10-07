class Solution(object):
    def reverse(self, x):
         
        
        sign = 1 if x > 0 else -1
        x = abs(x)
    
        reversed = 0
        while x > 0:
          reversed = reversed * 10 + x % 10
          x //= 10
        
        if reversed > 2**31-1 or reversed < -2**31:
            return 0
    
        return sign * reversed
            
        
        