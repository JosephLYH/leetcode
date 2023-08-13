from copy import deepcopy
from typing import Optional
from lib.linked_list import ListNode
import math


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return None

        p = head

        while p.next:
            p2 = p.next

            p.next = ListNode(math.gcd(p.val, p2.val))
            p.next.next = p2

            p = p2
            p2 = p2.next

        return head


testcases = []

solution = Solution()
for testcase in testcases:
    testcase_copy = deepcopy(testcase)
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
