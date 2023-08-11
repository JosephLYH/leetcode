from copy import deepcopy
from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        maximum = 0

        for num in arr:
            dp[num] = dp[num - difference] + 1
            maximum = max(maximum, dp[num])

        return maximum


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
