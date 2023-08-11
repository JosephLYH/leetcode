from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_len = len(nums) + 1
        sums = 0
        ps = 0

        for pf in range(len(nums)):
            sums += nums[pf]
            while sums >= target:
                min_len = min(min_len, pf - ps + 1)
                sums -= nums[ps]
                ps += 1

        return min_len if min_len <= len(nums) else 0


testcases = []
testcases.append([7, [2, 3, 1, 2, 4, 3], 2])
testcases.append([4, [1, 4, 4], 1])
testcases.append([11, [1, 1, 1, 1, 1, 1, 1, 1], 0])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
