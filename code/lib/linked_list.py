# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> list[int]:
        result = []
        temp = self
        while temp:
            result.append(temp.val)
            temp = temp.next
        return result

    def __str__(self) -> str:
        return str(self.to_list())


# Definition for creating a singly-linked list from a list of values.
class ListNodes:
    def __init__(self, vals=[]):
        if not vals:
            return None

        tail = ListNode(vals[-1], None)
        for val in reversed(vals[:-1]):
            tail = ListNode(val, tail)

        self.head = tail

    def to_list(self) -> list[int]:
        return self.head.to_list()


if __name__ == "__main__":
    print(ListNodes([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]).to_list())
