from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return 1 + area(r+1, c) + area(r-1, c) + area(r, c+1) + area(r, c-1)
        
        return max(area(r, c) for r in range(len(grid)) for c in range(len(grid[0])))
    
testcases = []
testcases.append(([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6))
testcases.append(([[0,0,0,0,0,0,0,0]], 0))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert False, f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'