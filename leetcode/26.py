class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx = idx + 1
        return idx


testcases = []
testcases.append(([1, 1, 2], 2))
testcases.append(([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5))

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
