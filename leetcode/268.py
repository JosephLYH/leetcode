from typing import List
from copy import deepcopy


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


testcases = []
testcases.append([[3, 0, 1], 2])
testcases.append([[0, 1], 2])
testcases.append([[9, 6, 4, 2, 3, 5, 7, 0, 1], 8])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
