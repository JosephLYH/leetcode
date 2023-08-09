from copy import deepcopy
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        count = 1
        prev_num = float("inf")

        for i in range(len(nums)):
            if nums[i] != prev_num:
                prev_num = nums[i]
                count = 1
            else:
                count += 1

            if count < 3:
                nums[p] = nums[i]
                p += 1

        return p


testcases = []
testcases.append([[1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]])
testcases.append([[0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]])

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
