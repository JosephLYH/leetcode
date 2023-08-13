from copy import deepcopy
from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximums = defaultdict(list)
        max_digits = list(map(lambda x: max(str(x)), nums))

        for i in range(len(nums)):
            maximums[max_digits[i]].append(nums[i])

        for key in maximums:
            if len(maximums[key]) < 2:
                maximums[key] = [-1]
            maximums[key].sort(reverse=True)
            maximums[key] = maximums[key][:2]

        return max(map(sum, maximums.values()))


testcases = []
testcases.append([[51, 71, 17, 24, 42], 88])
testcases.append([[1, 2, 3, 4], -1])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
