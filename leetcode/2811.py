from copy import deepcopy
from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] < m:
                count += 1

        if count == len(nums) - 1:
            return False

        return True


testcases = []

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
