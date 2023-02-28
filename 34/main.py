import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect.bisect_left(nums, target)
        return [left, bisect.bisect(nums, target)-1] if target in nums[left:left+1] else [-1, -1]
        
testcases = []
testcases.append(([5,7,7,8,8,10], 8, [3,4]))
testcases.append(([5,7,7,8,8,10], 6, [-1,-1]))
testcases.append(([], 0, [-1,-1]))
testcases.append(([1], 1, [0,0]))
testcases.append(([2,2], 2, [0,1]))
testcases.append(([1,2,2], 2, [1,2]))
testcases.append(([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4, [10,13]))

solution = Solution()
for nums, target, expected in testcases:
    assert solution.searchRange(nums, target) == expected, (nums, target, solution.searchRange(nums, target), expected)