from copy import deepcopy
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


testcases = []
testcases.append([[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11])
testcases.append([[[-10]], -10])

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
