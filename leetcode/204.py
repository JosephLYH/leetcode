import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        sieve = [1] * n
        sieve[0] = sieve[1] = 0

        for i in range(2, math.ceil(math.sqrt(n))):
            if sieve[i] == 1:
                for j in range(i * i, n, i):
                    sieve[j] = 0

        return sum(sieve)


testcases = []
testcases.append((10, 4))
testcases.append((0, 0))
testcases.append((1, 0))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
