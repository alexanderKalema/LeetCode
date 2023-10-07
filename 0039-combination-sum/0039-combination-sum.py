class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        ds = []


        def findCombination(ind, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                ds.pop()
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans