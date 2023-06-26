from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1] if i > 0 else grid[0][i]

        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp[-1][-1]
    
testcases = []
testcases.append(([[1,3,1],[1,5,1],[4,2,1]], 7))
testcases.append(([[1,2,3],[4,5,6]], 12))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert False, f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'