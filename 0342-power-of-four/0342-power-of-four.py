class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(x):
            if x == 1:
                return True
            if x <= 0 or x % 4 != 0:
                return False
            return power(x // 4)
        def powerl(l):
            if l == 1:
                return True
            if l >1 :
                return False
            else:
                return power(l*4)
        if n < 0:
            return powerl(n)
        else:
            return(power(n))