class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(l):
            if l == 0:
                return 1
            if l == 1:
                return x
            
            half = power(l // 2)
            
            if l % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1 / x
            n = -n
        
        return power(n)
