class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])
    
testcases = []
testcases.append(([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]))
testcases.append(([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1], testcase