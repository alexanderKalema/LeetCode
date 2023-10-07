class Solution(object):
    def uniquePaths(self, m, n):
        total = m + n -2
        choose = min(m, n) - 1
        product = 1
        for i in range(choose):
            product = product * total / (i+1)
            total -= 1
        return int(product) 