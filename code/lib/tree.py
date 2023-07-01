# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, nodes=None):
        if not nodes:
            return

        self.root = TreeNode(nodes[0])
        queue = [self.root]
        i = 1

        while queue:
            node = queue.pop(0)

            if i < len(nodes) and nodes[i]:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)

            i += 1
            if i < len(nodes) and nodes[i]:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)

            i += 1

    def to_list(self) -> list[int]:
        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result[-1] is None:
            result.pop()

        return result


if __name__ == "__main__":
    print(Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]).to_list())
