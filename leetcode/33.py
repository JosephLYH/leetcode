class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target < nums[0] < nums[mid]:  # -inf
                left = mid + 1
            elif target >= nums[0] > nums[mid]:  # +inf
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1


testcases = []
testcases.append([[4, 5, 6, 7, 0, 1, 2], 0, 4])
testcases.append([[4, 5, 6, 7, 0, 1, 2], 3, -1])
testcases.append([[1], 0, -1])

solution = Solution()
for testcase in testcases:
    assert (
        getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]
    ), testcase
