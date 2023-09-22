from typing import List
from copy import deepcopy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        # 2 ** len(nums) is the number of subsets
        # 1 << j is the jth bit
        # i & (1 << j) is the jth bit of i
        # if the jth bit of i is 1, then nums[j] is in the subset
        # if the jth bit of i is 0, then nums[j] is not in the subset
        for i in range(2 ** len(nums)):
            subset = []
            for j in range(len(nums)):
                if i & (1 << j):
                    subset.append(nums[j])
            subsets.append(subset)

        return subsets


testcases = []
testcases.append([[1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]])
testcases.append([[0], [[], [0]]])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
