from copy import deepcopy
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        stack = []
        output = []
        idx = -1

        for word in words:
            if word != "prev":
                stack.append(int(word))
                idx = len(stack) - 1
            else:
                output.append(stack[idx] if idx >= 0 else -1)
                idx -= 1

        return output


testcases = []

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
