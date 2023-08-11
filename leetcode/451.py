class Solution:
    def frequencySort(self, s: str) -> str:
        self.freq = {}

        for char in s:
            self.freq[char] = self.freq.get(char, 0) + 1

        self.freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

        return "".join([char * freq for char, freq in self.freq])


testcases = []
testcases.append(["tree", "eetr"])
testcases.append(["cccaaa", "cccaaa"])
testcases.append(["Aabb", "bbAa"])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
