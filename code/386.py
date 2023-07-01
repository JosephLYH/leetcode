from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num):
            num = num * 10
            if num > n:
                return []

            result = []
            for i in range(num, num + 10):
                if i <= n:
                    result.extend([i])
                    result.extend(dfs(i))

            return result

        result = []
        for i in range(1, 10):
            if i <= n:
                result.extend([i])
                result.extend(dfs(i))

        return result


testcases = []
testcases.append((13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]))
testcases.append((2, [1, 2]))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
