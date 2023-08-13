from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        seen = set()
        queue = [(0, 0, 1)]

        while queue:
            x, y, steps = queue.pop(0)

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return steps

            if (x, y) in seen:
                continue

            seen.add((x, y))
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == j == 0:
                        continue

                    if (
                        0 <= x + i < len(grid)
                        and 0 <= y + j < len(grid[0])
                        and grid[x + i][y + j] == 0
                    ):
                        queue.append((x + i, y + j, steps + 1))

        return -1


testcases = []
testcases.append([[[0, 1], [1, 0]], 2])
testcases.append([[[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4])
testcases.append([[[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
