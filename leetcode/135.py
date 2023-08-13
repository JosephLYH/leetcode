from copy import deepcopy
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        counter = 0
        candies = [1] * len(ratings)
        for i, rating in enumerate(ratings):
            if i > 0 and rating > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 1, -1, -1):
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


testcases = []
testcases.append([[1, 0, 2], 5])
testcases.append([[1, 2, 2], 4])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
