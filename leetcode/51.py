from copy import deepcopy
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        stack = []
        self.result = []

        def backtrack(row):
            if row == n:
                addSolution()
                return

            for col in range(n):
                if col not in stack:
                    if all(abs(col - c) != row - i for i, c in enumerate(stack)):
                        stack.append(col)
                        backtrack(row + 1)
                        stack.pop()

        def addSolution():
            self.result.append(
                ["".join("Q" if i == col else "." for i in range(n)) for col in stack]
            )

        backtrack(0)

        return self.result


testcases = []
testcases.append(
    [4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]]
)
testcases.append([1, [["Q"]]])

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
