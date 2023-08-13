from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]


testcases = []
testcases.append([2, [0, 1, 1]])
testcases.append([5, [0, 1, 1, 2, 1, 2]])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
