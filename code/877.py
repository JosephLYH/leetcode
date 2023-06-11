class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return True
    
testcases = []
testcases.append(([5,3,4,5], True))
testcases.append(([3,7,2,3], True))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1], testcase