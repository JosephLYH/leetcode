from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i - 1])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


testcases = []
testcases.append(([1, 2, 3, 1], 4))
testcases.append(([2, 7, 9, 3, 1], 12))
testcases.append(([2, 1, 1, 2], 4))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
