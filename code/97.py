from collections import defaultdict

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # determine in O(len(s1 + s2)) if False
        counts = defaultdict(lambda: 0)
        for letter in s1: counts[letter] += 1
        for letter in s2: counts[letter] += 1

        counts2 = defaultdict(lambda: 0)
        for letter in s3: counts2[letter] += 1

        for letter in counts:
            if counts[letter] != counts2[letter]: return False

        
    
testcases = []
testcases.append(('aabcc', 'dbbca', 'aadbbcbcac', True))
testcases.append(('aabcc', 'dbbca', 'aadbbbaccc', False))
testcases.append(('', '', '', True))
testcases.append(('a', '', 'a', True))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert output == testcase[-1], f'testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}'