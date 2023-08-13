from copy import deepcopy
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0

        arr, best_dist = SortedList([]), float("inf")
        for i in range(x, len(nums)):
            arr.add(nums[i - x])
            v = nums[i]

            pos = arr.bisect_left(v)
            if pos < len(arr):
                best_dist = min(best_dist, abs(arr[pos] - v))
            if pos > 0:
                best_dist = min(best_dist, abs(arr[pos - 1] - v))

        return best_dist


testcases = []
testcases.append(([4, 3, 2, 4], 2, 0))
testcases.append(([5, 3, 2, 10, 15], 1, 1))
testcases.append(([1, 2, 3, 4], 3, 3))

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
