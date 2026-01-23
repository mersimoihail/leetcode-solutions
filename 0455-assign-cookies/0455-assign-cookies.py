class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ch = 0
        co = 0
        cn = 0
        s.sort()
        g.sort()
        while ch < len(s):
            if co <len(g):
                while ch <len(s) and s[ch] < g[co]:
                    ch += 1
            if ch <len(s) and co <len(g) and s[ch] >=g[co]:
                cn += 1
                    
            ch +=1
            co +=1
        return cn
            

                    