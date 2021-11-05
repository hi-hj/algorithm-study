from collections import deque

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.queue = deque()
        for i in range(len(encoding)//2):
            cnt = encoding[i*2]
            num = encoding[i*2+1]
            if cnt==0: continue
            self.queue.append([cnt, num])

    def next(self, n: int) -> int:
        while n:
            if not self.queue: return -1
            if n >= self.queue[0][0]:
                n -= self.queue[0][0]
                last = self.queue[0][1]
                self.queue.popleft()
            else:
                self.queue[0][0] -=n
                return self.queue[0][1]
        return last


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)