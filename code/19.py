from typing import Optional
from lib.linked_list import ListNode, ListNodes, node_to_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ps, pf = head, head

        for _ in range(n):
            pf = pf.next

        while True:
            if pf and pf.next:
                ps, pf = ps.next, pf.next
            else:
                break

        if ps == head and pf == None:
            head = head.next
        else:
            ps.next = ps.next.next

        return head


testcases = []
testcases.append((ListNodes([1, 2, 3, 4, 5]).head, 2, [1, 2, 3, 5]))
testcases.append((ListNodes([1]).head, 1, []))
testcases.append((ListNodes([1, 2]).head, 1, [1]))

solution = Solution()
for testcase in testcases:
    assert (
        node_to_list(getattr(solution, dir(solution)[-1])(*testcase[:-1]))
        == testcase[-1]
    )
