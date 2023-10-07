class Solution(object):
    def isPalindrome(self, x):
        org = x
        rev = 0 
        
        while(x>0): 
            rev = rev*10 + x %10
            x//=10 
            
        if(rev == org):
            return True
        else:
            return False
           
        
        