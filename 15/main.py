class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        positives = {}
        negatives = {}
        zeros = 0
        results = set()

        for num in nums:
            if num == 0:
                zeros += 1
            elif num > 0:
                positives[num] = positives.get(num, 0) + 1
            else:
                negatives[num] = negatives.get(num, 0) + 1

        if zeros >= 3:
            results.add((0, 0, 0))
        
        for positive in positives:
            for negative in negatives:
                if zeros > 0 and positive + negative == 0:
                    results.add((negative, 0, positive))
                    continue

                # negation of positive + negative
                negation = -positive - negative
                if (negation == positive and positives[positive] < 2) or (negation == negative and negatives[negative] < 2):
                    continue
                
                if negation in positives or negation in negatives:
                    results.add(tuple(sorted([negative, negation, positive])))

        return list(map(lambda x: list(x), results))
        
testcases = []
testcases.append(([-1,0,1,2,-1,-4], [[-1,0,1], [-1,-1,2]]))
testcases.append(([0, 1, 1], []))
testcases.append(([0, 0, 0], [[0, 0, 0]]))

solution = Solution()
for testcase in testcases:
    assert getattr(solution, dir(solution)[-1])(*testcase[:-1]) == testcase[-1]