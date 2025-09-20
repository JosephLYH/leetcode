from copy import deepcopy
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:


testcases = []
testcases.append([[7,1,5,3,6,4], 7])
testcases.append([[7,6,4,3,1], 4])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
