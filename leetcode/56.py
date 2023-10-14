from copy import deepcopy
from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        output = []
        for interval in intervals:
            if output:
                if output[-1][1] >= interval[0]:
                    output[-1][1] = max(output[-1][1], interval[1])
                else:
                    output.append(interval)
            else:
                output.append(interval)

        return output


testcases = []
testcases.append([[[2, 6], [1, 3], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]])
testcases.append([[[1, 4], [4, 5]], [[1, 5]]])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
