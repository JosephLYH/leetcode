class SmallestInfiniteSet:
    def __init__(self):
        self.added = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.added:
            temp = min(self.added)
            self.added.remove(temp)
            return temp

        self.current += 1
        return self.current - 1

    def addBack(self, num: int) -> None:
        if self.current > num:
            self.added.add(num)
