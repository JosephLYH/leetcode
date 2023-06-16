class Solution:
    def template(self):
        raise NotImplementedError
    
testcases = []

solution = Solution()
for testcase in testcases:
    result = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert result == testcase[-1], (*testcase, result)