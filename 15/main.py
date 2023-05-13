class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

    
testcases = []
testcases.append(([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]))
testcases.append(([0, 1, 1], []))
testcases.append(([0, 0, 0], [[0, 0, 0]]))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]