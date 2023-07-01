class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix, low = [], n * n + 1
        while low > 1:
            low, high = low - len(matrix), low
            matrix = [list(range(low, high))] + list(
                map(lambda x: list(x), [*zip(*matrix[::-1])])
            )
        return matrix


testcases = []
testcases.append((3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
testcases.append((2, [[1, 2], [4, 3]]))
testcases.append((1, [[1]]))

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
