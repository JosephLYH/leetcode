from copy import deepcopy
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        max_y, max_x = len(grid), len(grid[0])

        start = None
        for y in range(max_y):
            for x in range(max_x):
                self.count += grid[y][x] == 0
                if not start and grid[y][x] == 1:
                    start = (x, y)

        def backtrack(i, j):
            result = 0
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < max_x and 0 <= y < max_y:
                    if grid[y][x] == 0:
                        grid[y][x] = -1
                        self.count -= 1
                        result += backtrack(x, y)
                        grid[y][x] = 0
                        self.count += 1
                    elif grid[y][x] == 2:
                        result += self.count == 0
            return result

        return backtrack(start[0], start[1])


testcases = []
testcases.append(([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2))
testcases.append(([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4))
testcases.append(([[0, 1], [2, 0]], 0))
testcases.append(([[0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], 1))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(deepcopy(*testcase[:-1]))
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
