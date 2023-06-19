from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cumsum = sum(nums)
        target = cumsum - x

        ps, pf = 0, 0
        sums = 0
        max_len = -1
        while pf < len(nums):
            sums += nums[pf]
            while sums > target and ps <= pf:
                sums -= nums[ps]
                ps += 1
            if sums == target:
                max_len = max(max_len, pf - ps + 1)
            pf += 1

        return len(nums) - max_len if max_len != -1 else -1
    
testcases = []
testcases.append(([1,1,4,2,3], 5, 2))
testcases.append(([5,6,7,8,9], 4, -1))
testcases.append(([3,2,20,1,1,3], 10, 5))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert output == testcase[-1], f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'