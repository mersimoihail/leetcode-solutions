class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while len(s) < k+1:
            s += "1"
            pointer = len(s)-2
            while pointer >=0:
                if s[pointer] == "0":
                    s+="1"
                else:
                    s+="0"
                pointer -=1
        print(s)
        return s[k-1]
        
        