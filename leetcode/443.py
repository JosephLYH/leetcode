from copy import deepcopy
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, res = 0, 0

        while i < len(chars):
            group_length = 1

            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1

            chars[res] = chars[i]
            res += 1

            if group_length > 1:
                str_repr = str(group_length)
                chars[res : res + len(str_repr)] = list(str_repr)
                res += len(str_repr)

            i += group_length

        return res


testcases = []

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(deepcopy(*testcase[:-1]))
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
