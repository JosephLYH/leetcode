from typing import Optional
from lib.linked_list import ListNode, ListNodes


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        temp_head = head

        while True:
            if not head.next:
                break
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return temp_head


testcases = []
testcases.append((ListNodes([1, 1, 2]).head, [1, 2]))
testcases.append((ListNodes([1, 1, 2, 3, 3]).head, [1, 2, 3]))

solution = Solution()
for testcase in testcases:
    result = getattr(solution, dir(solution)[-1])(*testcase[:-1]).to_list()
    assert result == testcase[-1], (*testcase, result)
