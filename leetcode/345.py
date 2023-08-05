class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])

        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            while left < right and s[left].lower() not in vowels:
                left += 1
            while left < right and s[right].lower() not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)


testcases = []
testcases.append(("hello", "holle"))
testcases.append(("leetcode", "leotcede"))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
