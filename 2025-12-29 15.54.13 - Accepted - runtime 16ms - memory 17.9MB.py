class SmallestInfiniteSet:
    def __init__(self):
        self.cur = 1
        self.s = set()

    def popSmallest(self) -> int:
        if self.s:
            res = min(self.s)
            self.s.remove(res)
            return res
        self.cur += 1
        return self.cur - 1

    def addBack(self, num: int) -> None:
        if num < self.cur:
            self.s.add(num)