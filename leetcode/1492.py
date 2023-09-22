import math
from copy import deepcopy


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_small = []
        factors_large = []
        for factor_small in range(1, math.floor(math.sqrt(n + 1)) + 1):
            if n % factor_small == 0:
                factors_small.append(factor_small)

                factor_large = n // factor_small
                if factor_small != factor_large:
                    factors_large.append(factor_large)

        if k <= len(factors_small):
            return factors_small[k - 1]
        elif k <= len(factors_small) + len(factors_large):
            return factors_large[len(factors_large) - (k - len(factors_small))]

        return -1


testcases = []
testcases.append([12, 3, 3])
testcases.append([7, 2, 7])
testcases.append([4, 4, -1])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
