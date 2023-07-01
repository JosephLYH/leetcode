from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixs = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefixs[i+1] = prefixs[i] + nums[i]

        averages = [-1] * len(nums)
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                averages[i] = (prefixs[i+k+1] - prefixs[i-k]) // (2*k + 1)

        return averages
    
testcases = []
testcases.append(([7,4,3,9,1,8,5,2,6], 3, [-1,-1,-1,5,4,4,-1,-1,-1]))
testcases.append(([100000], 0, [100000]))
testcases.append(([8], 100000, [-1]))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert False, f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'