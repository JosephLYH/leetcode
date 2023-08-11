class Solution:
    def intToRoman(self, num: int) -> str:
        list_map_1000 = ["", "M", "MM", "MMM"]
        list_map_100 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        list_map_10 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        list_map_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            list_map_1000[num // 1000]
            + list_map_100[num % 1000 // 100]
            + list_map_10[num % 100 // 10]
            + list_map_1[num % 10]
        )


testcases = []
testcases.append([3, "III"])
testcases.append([58, "LVIII"])
testcases.append([1994, "MCMXCIV"])

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
