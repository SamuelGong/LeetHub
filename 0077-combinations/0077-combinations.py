class Solution:
    def __init__(self):
        self.result = []
        self.path = []
        
    def backtracking(self, b, e, k):
        for i in range(b, e):
            self.path.append(i)
            if len(self.path) == k:
                self.result.append([e for e in self.path])
            else:
                self.backtracking(i + 1, e, k)
            self.path.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(1, n + 1, k)
        return self.result