class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] = -1
            else:
                seen[s[i]] = i

        minimum = len(s)
        for key in seen:
            if seen[key] != -1:
                minimum = min(minimum, seen[key])

        return minimum if minimum != len(s) else -1


testcases = []
testcases.append(["leetcode", 0])
testcases.append(["loveleetcode", 2])
testcases.append(["aabb", -1])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
