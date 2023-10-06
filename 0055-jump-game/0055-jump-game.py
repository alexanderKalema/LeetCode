class Solution(object):
    def canJump(self, nums):
        goal = len(nums)-1
        for index in range(len(nums)-1, -1, -1):
            if( goal <= index + nums[index]):
                goal = index
            else:
                continue
        if(goal == 0):
            return True
        else:
            return False
        