class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        
        for i in range(len(nums)):
            num_map[nums[i]] -= 1
            
            for j in range(i+1, len(nums)):
                num_map[nums[j]] -= 1

                if num_map.get(-nums[i]-nums[j], 0) > 0:
                    result.append([nums[i], nums[j], -nums[i]-nums[j]])

                
                num_map[nums[j]] += 1
            
            num_map[nums[i]] += 1

        return result
    
testcases = []
testcases.append(([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]))
testcases.append(([0, 1, 1], []))
testcases.append(([0, 0, 0], [[0, 0, 0]]))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]