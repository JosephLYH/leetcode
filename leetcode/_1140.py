import numpy as np


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        memory = np.zeros((2, len(piles), len(piles)))

        def dp(player, idx, m):
            if not memory[player, idx, m] == 0:
                return memory[player, idx, m]

            if m >= len(piles) - idx:
                return sum(piles[idx:])

            for next_m in range(1, 2 * m + 1):
                return max([dp(player)])
            return

        return None


testcases = []
testcases.append([[2, 7, 9, 4, 4], 10])
testcases.append([[1, 2, 3, 4, 5, 100], 104])

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
