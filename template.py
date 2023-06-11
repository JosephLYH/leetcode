class Solution:
    def template(self):
        raise NotImplementedError
    
testcases = []

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]