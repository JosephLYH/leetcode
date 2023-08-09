from copy import deepcopy


class Solution:
    def finalString(self, s: str) -> str:
        final = ""
        substrings = s.split("i")
        for substring in substrings:
            final = final[::-1] + substring

        return final


testcases = []

solution = Solution()
for testcase in testcases:
    testcase = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
