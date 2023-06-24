from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        max_length = 0
        for num in freq:
            if num + 1 in freq:
                max_length = max(max_length, freq[num] + freq[num + 1])

        return max_length

        
testcases = []
testcases.append([[1,3,2,2,5,2,3,7], 5])
testcases.append([[1,2,3,4], 2])
testcases.append([[1,1,1,1], 0])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert False, f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'