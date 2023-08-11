from copy import deepcopy
from typing import List
from collections import defaultdict


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n])

        live = batteries[-n:]

        for i in range(n - 1):
            if extra // (i + 1) < live[i + 1] - live[i]:
                return live[i] + extra // (i + 1)

            extra -= (i + 1) * (live[i + 1] - live[i])

        return live[-1] + extra // n


testcases = []
testcases.append([2, [3, 3, 3], 4])
testcases.append([2, [1, 1, 1, 1], 2])


solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
