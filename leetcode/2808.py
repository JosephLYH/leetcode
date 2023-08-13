from copy import deepcopy
from typing import List
from collections import defaultdict


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        nums += nums

        values_idx = defaultdict(list)
        for i, num in enumerate(nums):
            values_idx[num].append(i)
        if len(values_idx) == 1:
            return 0

        min_moves = float("inf")

        for value, idxs in values_idx.items():
            dists = list(map(lambda x, y: x - y, idxs + [0], [0] + idxs))[1:-1]
            min_dist = max(dists) // 2
            if min_dist < min_moves:
                min_moves = min_dist

        return min_moves


testcases = []
testcases.append([[1, 2, 1, 2], 1])
testcases.append([[2, 1, 3, 3, 2], 2])
testcases.append([[5, 5, 5, 5, 5], 0])
testcases.append([[8, 13, 3, 3], 1])
testcases.append([[8, 8, 9, 10, 9], 1])
testcases.append([[1, 11, 11, 11, 19, 12, 8, 7, 19], 2])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
