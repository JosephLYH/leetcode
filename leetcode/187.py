from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        repeated = []

        for i in range(len(s) - 9):
            if seen[s[i : i + 10]] > 0:
                seen[s[i : i + 10]] += 1
                if seen[s[i : i + 10]] == 2:
                    repeated.append(s[i : i + 10])
            else:
                seen[s[i : i + 10]] = 1

        return repeated


testcases = []
testcases.append(["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]])
testcases.append(["AAAAAAAAAAAAA", ["AAAAAAAAAA"]])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
