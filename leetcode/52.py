from copy import deepcopy
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        stack = []
        self.count = 0

        def backtrack(row):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if col not in stack:
                    if all(abs(col - c) != row - i for i, c in enumerate(stack)):
                        stack.append(col)
                        backtrack(row + 1)
                        stack.pop()

        backtrack(0)

        return self.count


testcases = []
testcases.append([4, 2])
testcases.append([1, 1])

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
