from copy import deepcopy
from typing import Optional
from lib.linked_list import ListNode, ListNodes


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def doubleItSub(curr):
            if not curr:
                return 0

            carry, curr.val = divmod(curr.val * 2 + doubleItSub(curr.next), 10)

            return carry

        if not head:
            return None

        carry, head.val = divmod(head.val * 2 + doubleItSub(head.next), 10)
        if carry > 0:
            head = ListNode(carry, head)

        return head


testcases = []
testcases.append([ListNodes([1, 2, 3]).head, [2, 4, 6]])
testcases.append([ListNodes([1, 8, 9]).head, [3, 7, 8]])
testcases.append([ListNodes([9, 9, 9]).head, [1, 9, 9, 8]])

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1]).to_list()
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1]).to_list()
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
