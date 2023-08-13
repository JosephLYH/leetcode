class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


testcases = []
testcases.append(["the sky is blue", "blue is sky the"])
testcases.append(["  hello world!  ", "world! hello"])
testcases.append(["a good   example", "example good a"])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
