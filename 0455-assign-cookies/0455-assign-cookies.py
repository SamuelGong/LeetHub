class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        
        t = 0
        si = 0
        sorted_s = sorted(s)
        for e in sorted(g):
            if sorted_s[-1] < e:
                break

            while si < len(sorted_s):
                si += 1
                if sorted_s[si - 1] >= e:
                    t += 1
                    break
        return t
