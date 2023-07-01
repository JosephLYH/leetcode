class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp = 0

        for char in s:
            temp ^= ord(char)

        for char in t:
            temp ^= ord(char)

        return chr(temp)


testcases = []
testcases.append(("abcd", "abcde", "e"))
testcases.append(("", "y", "y"))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
