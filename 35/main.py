class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
        
testcases = []
testcases.append(([1,3,5,6], 5, 2))
testcases.append(([1,3,5,6], 2, 1))
testcases.append(([1,3,5,6], 7, 4))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]