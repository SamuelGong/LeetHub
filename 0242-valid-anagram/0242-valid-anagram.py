class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s_d = {}
        for c in s:
            if c not in s_d:
                s_d.update({c: 1})
            else:
                s_d[c] += 1
        
        t_d = {}
        for c in t:
            if c not in t_d:
                t_d.update({c: 1})
            else:
                t_d[c] += 1
        
        for c in sorted(list(s_d.keys())):
            if c not in t_d:
                return False
            
            if not s_d[c] == t_d[c]:
                return False
        
        return True