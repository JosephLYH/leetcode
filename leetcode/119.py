from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        row = self.getRow(rowIndex - 1)
        return [sum(x) for x in zip(row + [0], [0] + row)]


testcases = []
testcases.append((3, [1, 3, 3, 1]))
testcases.append((0, [1]))
testcases.append((1, [1, 1]))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
