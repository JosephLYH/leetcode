from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_dict = {}
        positions = {}
        max_pos = 0
        for course, prerequisite in prerequisites:
            if course not in prerequisites_dict:
                prerequisites_dict[course] = []
            prerequisites_dict[course].append(prerequisite)

            course_pos = 0
            if prerequisite not in positions:
                positions[prerequisite] = max_pos
                max_pos += 1
            if course not in positions:
                positions[course] = max_pos
                max_pos += 1
        return []


testcases = []
testcases.append((2, [[1, 0]], [0, 1]))
testcases.append((4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]))

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    assert (
        output == testcase[-1]
    ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
