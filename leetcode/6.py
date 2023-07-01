class Solution:
    def convert(self, s: str, numRows: int) -> str:
        print_str = s[:: max(numRows * 2 - 2, 1)]
        for i in range(1, numRows - 1):
            p1 = s[i :: max(numRows * 2 - 2, 1)]
            p2 = s[(numRows * 2 - 2) - i :: max(numRows * 2 - 2, 1)]
            mid = [x for y in zip(p1, p2) for x in y]
            if len(p1) > len(p2):
                mid.append(p1[-1])
            print_str += "".join(mid)
        if numRows > 1:
            print_str += s[numRows - 1 :: max(numRows * 2 - 2, 1)]

        return print_str


testcases = []
testcases.append(("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"))
testcases.append(("PAYPALISHIRING", 4, "PINALSIGYAHRPI"))
testcases.append(("A", 1, "A"))

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
