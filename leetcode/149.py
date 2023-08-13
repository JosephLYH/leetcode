from copy import deepcopy
from typing import List
from collections import defaultdict
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(int)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    slopes[(float("inf"), float("inf"))] += 1
                else:
                    y = y2 - y1
                    x = x2 - x1
                    gcd = math.gcd(y, x)
                    slopes[(y /= gcd, x /= gcd)] += 1

        return max(slopes.values())


testcases = []
testcases.append([[[1, 1], [2, 2], [3, 3]], 3])
testcases.append([[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
