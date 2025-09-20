from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return


testcases = []
testcases.append([[2, 1, 5, 6, 2, 3], 10])
testcases.append([[2, 4], 4])

solution = Solution()
for testcase in testcases:
    result = getattr(solution, dir(solution)[-1])(*testcase[:-1]).to_list()
    assert result == testcase[-1], (*testcase, result)
