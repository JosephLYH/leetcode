from copy import deepcopy
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)

        for citation in citations:
            counts[min(citation, n)] += 1

        total = 0
        for i in range(n, -1, -1):
            total += counts[i]
            if total >= i:
                return i

        return 0


testcases = []
testcases.append([[3, 0, 6, 1, 5], 3])
testcases.append([[1, 3, 1], 1])
testcases.append([[0], 0])
testcases.append([[1], 1])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
