class Solution(object):
    def lengthOfLongestSubstring(self, s):
        pure = set()
        left = 0
        res = 0
        
        
        for index in range(len(s)):
            while s[index] in pure:
                pure.remove(s[left])
                left += 1
            pure.add(s[index])
            res = max(res, index - left + 1)
            
        return res    
               
                
             
            
            