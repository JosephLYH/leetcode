from copy import deepcopy


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[n]


testcases = []
testcases.append([3, 5])
testcases.append([1, 1])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
