class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        self.target = 0
        self.quota = 0
    
    def backtracking(self, b):
        min_sum = sum([i for i in range(b, b + (self.quota - len(self.path)))])
        if min_sum > self.target - sum(self.path):
            return
        max_sum = sum([i for i in range(9, 9 - (self.quota - len(self.path)), -1)])
        if max_sum < self.target - sum(self.path):
            return

        for i in range(b, 10):
            self.path.append(i)
            if len(self.path) == self.quota:
                if sum(self.path) == self.target:
                    self.result.append([e for e in self.path])
            else:
                self.backtracking(i + 1)
            self.path.pop()
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.target = n
        self.quota = k
        self.backtracking(1)
        return self.result
