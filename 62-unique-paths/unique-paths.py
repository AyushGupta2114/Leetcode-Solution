class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # return math.comb(m+n-2, m-1) 
        @cache
        def dfs(i,j):
            if i==m-1 or j==n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)