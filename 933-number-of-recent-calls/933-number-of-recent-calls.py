class RecentCounter:

    def __init__(self):
        self.reqs = [None]
        self.prev_ind = 0
        self.prev_t = self.reqs[0]

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        if self.prev_t is None:
            self.prev_t = t
            self.prev_ind = 1
            return 1
        if t - 3000 <= self.prev_t:
            return len(self.reqs) - self.prev_ind
        for i, el in enumerate(self.reqs[self.prev_ind :]):
            if el >= t - 3000:
                self.prev_t = el
                self.prev_ind += i
                break
        return len(self.reqs) - self.prev_ind
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)