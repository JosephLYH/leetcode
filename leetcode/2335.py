from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)


testcases = []
testcases.append([[1, 4, 2], 4])
testcases.append([[5, 4, 4], 7])
testcases.append([[5, 0, 0], 5])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
