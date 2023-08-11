from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0

        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                planted += 1

        return planted >= n


testcases = []
testcases.append([[1, 0, 0, 0, 1], 1, True])
testcases.append([[1, 0, 0, 0, 1], 2, False])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
