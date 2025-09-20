from copy import deepcopy
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        return


testcases = []
testcases.append([[10, 1, 2, 7, 1, 3], 2, 1])
testcases.append([[4, 2, 1, 2], 1, 0])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
