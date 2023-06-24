class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        length = len(self.queue)
        self.queue.append(x)
        
        for _ in range(length):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0