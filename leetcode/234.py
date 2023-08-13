from typing import Optional
from lib.linked_list import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        p = head

        # get length
        while p:
            length += 1
            p = p.next

        # if length == 0 or 1, return True
        if length <= 1:
            return True

        # find second half of linked list
        head2 = head
        for _ in range(length // 2 if length % 2 == 0 else length // 2 + 1):
            head2 = head2.next

        # reverse second half of linked list
        curr = head2
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # compare first half and reversed second half
        p1 = head
        p2 = prev
        for _ in range(length // 2):
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


testcases = []

solution = Solution()
for testcase in testcases:
    output = getattr(solution, dir(solution)[-1])(*testcase[:-1])
    if output != testcase[-1]:
        getattr(solution, dir(solution)[-1])(*testcase_copy[:-1])
        assert (
            False
        ), f"testcase: {testcase[:-1]}, expected: {testcase[-1]}, output: {output}"
