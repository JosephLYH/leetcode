from typing import List, Optional
from lib.tree import TreeNode, Tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        queue = [(root, [root.val])]
        result = []

        while queue:
            node, path = queue.pop(0)

            if not node.left and not node.right and sum(path) == targetSum:
                result.append(path)

            if node.left:
                queue.append((node.left, path + [node.left.val]))

            if node.right:
                queue.append((node.right, path + [node.right.val]))

        return result


testcases = []
testcases.append(
    (
        Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]).root,
        22,
        [[5, 4, 11, 2], [5, 8, 4, 5]],
    )
)
testcases.append([Tree([1, 2, 3]).root, 5, []])
testcases.append([Tree([1, 2]).root, 0, []])

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
