from copy import deepcopy
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i - zeros] = nums[i]

        for i in range(len(nums) - zeros, len(nums)):
            nums[i] = 0

        return nums


testcases = []
testcases.append([[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]])
testcases.append([[0], [0]])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
