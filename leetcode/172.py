class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 5 * 2 = 10
        # 2 is always more than 5
        # so we only need to count 5
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


testcases = []
testcases.append([3, 0])
testcases.append([5, 1])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
