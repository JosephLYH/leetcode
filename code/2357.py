from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num > 0 and num not in seen:
                seen.add(num)

        return len(seen)


testcases = []
testcases.append(([1, 5, 0, 3, 5], 3))
testcases.append(([0], 0))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
