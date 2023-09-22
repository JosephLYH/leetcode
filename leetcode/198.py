from typing import List
from copy import deepcopy


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_len = len(grid) - 1
        y_len = len(grid[0]) - 1

        def bfs(i, j):
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            bfs(max(0, i - 1), j)
            bfs(min(x_len, i + 1), j)
            bfs(i, max(0, j - 1))
            bfs(i, min(y_len, j + 1))

        count = 0
        for i in range(x_len + 1):
            for j in range(y_len + 1):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count


testcases = []
testcases.append(
    (
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    )
)
testcases.append(
    (
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    )
)

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
