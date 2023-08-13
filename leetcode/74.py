from copy import deepcopy
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_max = len(matrix)
        x_max = len(matrix[0])

        def getIdx(r, c):
            return r * x_max + c

        def getRC(idx):
            return int(idx // x_max), int(idx % x_max)

        left, right = 0, y_max * x_max - 1
        while left <= right:
            r, c = getRC((left + right) // 2)

            if target > matrix[r][c]:
                left = getIdx(r, c) + 1
            elif target < matrix[r][c]:
                right = getIdx(r, c) - 1
            else:
                return True

        return False


testcases = []
testcases.append([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True])
testcases.append([[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
