# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

from typing import List
from copy import deepcopy


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if answerKey == "":
            return 0

        counts = {"T": 0, "F": 0}

        left = 0
        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            if counts["T"] > k and counts["F"] > k:
                counts[answerKey[left]] -= 1
                left += 1

        return right + 1 - left


testcases = []
testcases.append(["TTFF", 2, 4])
testcases.append(["TFFT", 1, 3])
testcases.append(["TTFTTFTT", 1, 5])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
