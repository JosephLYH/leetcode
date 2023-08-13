class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i

        return n == 1


testcases = []
testcases.append([6, True])
testcases.append([1, True])
testcases.append([14, False])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
