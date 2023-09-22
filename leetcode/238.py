from typing import List
from copy import deepcopy


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0 and zero_count == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count == 0:
            for i in range(len(nums)):
                nums[i] = product // nums[i]
        else:
            for i in range(len(nums)):
                nums[i] = 0 if nums[i] != 0 else product

        return nums


testcases = []
testcases.append([[1, 2, 3, 4], [24, 12, 8, 6]])
testcases.append([[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
