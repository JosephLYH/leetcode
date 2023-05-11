class Solution:
    def template(self):
        pass
    
testcases = []

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]