from copy import deepcopy
from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        if sum(nums2) - max(nums2) > x:
            return -1

        def step(nums, x, count):
            nums = deepcopy(nums)
            if sum(nums) <= x:
                return count

            nums = list(map(lambda x, y: x + y, nums, nums2))

            min_count = float("inf")
            for i in range(len(nums)):
                min_count = min(
                    min_count, step(nums[:i] + [0] + nums[i + 1 :], x, count + 1)
                )

        return step(nums1, x, 0)


testcases = []
testcases.append([[1, 2, 3], [1, 2, 3], 4, 3])
testcases.append([[1, 2, 3], [3, 3, 3], 4, -1])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)

    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
