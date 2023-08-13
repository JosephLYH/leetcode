from copy import deepcopy
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])

        return dp[0] >= 0


testcases = []
testcases.append([[1, 5, 2], False])
testcases.append([[1, 5, 233, 7], True])
testcases.append([[0, 0, 7, 6, 5, 6, 1], False])


solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
