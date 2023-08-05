from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)

        return [candy + extraCandies >= maximum for candy in candies]


testcases = []
testcases.append(([2, 3, 5, 1, 3], 3, [True, True, True, False, True]))
testcases.append(([4, 2, 1, 1, 2], 1, [True, False, False, False, False]))
testcases.append(([12, 1, 12], 10, [True, False, True]))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
