from copy import deepcopy
from typing import List


class Solution:
    def getWordsInLongestSubsequence(
        self, n: int, words: List[str], groups: List[int]
    ) -> List[str]:
        idxs = []
        output = []

        prev = -1
        for i in range(len(groups)):
            if groups[i] != prev:
                output.append(words[i])
                prev = groups[i]

        return output


testcases = []

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
