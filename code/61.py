from typing import Optional
from lib.linked_list import ListNode, ListNodes

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k == 0: return head

        tail = head
        length = 1

        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        tail.next = head
        
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        head, temp.next = temp.next, None
        return head
    
testcases = []
testcases.append((ListNodes([1,2,3,4,5]).head, 2, [4,5,1,2,3]))
testcases.append((ListNodes([0,1,2]).head, 4, [2,0,1]))
testcases.append((ListNodes([1]).head, 99, [1]))
testcases.append((ListNodes([1, 2]).head, 1, [2, 1]))
 
solution = Solution()
for testcase in testcases:
    result = getattr(solution, dir(solution)[-1])(*testcase[:-1]).to_list()
    assert result == testcase[-1], (*testcase, result)