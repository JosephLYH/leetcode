class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for i, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], i]
            mapping[num] = i
        return


testcases = []
testcases.append(([2, 7, 11, 15], 9, [0, 1]))

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
