from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        count = 0
        total = 0
        for num, f in freq:
            count += 1
            total += f
            if total >= len(arr) // 2:
                return count


testcases = []
testcases.append([[3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2])
testcases.append([[7, 7, 7, 7, 7, 7], 1])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
