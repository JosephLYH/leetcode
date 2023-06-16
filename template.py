class Solution:
    def template(self):
        raise NotImplementedError
    
testcases = []

solution = Solution()
for testcase in testcases:
    result = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert output == testcase[-1], f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'